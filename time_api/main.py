from datetime import datetime, timedelta
import logging
import os
from zoneinfo import ZoneInfo

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
logger = logging.getLogger("fiach.time_api")

app = FastAPI(
    title="FIACH Time API",
    version="1.0.0",
    description="API simple para entregar fecha, hora y dia actual en zona horaria de Chile.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TZ = ZoneInfo("America/Santiago")
GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_ENDPOINT = (
    f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
)
FIACH_SYSTEM_PROMPT = (
    "Eres FIACH, acompanante pedagogico para docentes chilenos. "
    "Principio central: no aumentar carga docente innecesariamente. "
    "Si la practica funciona, no intervengas. Maximo 1-2 ajustes simples. "
    "Tono cercano, humano, breve. Contexto chileno: curriculum MINEDUC."
)

WEEKDAYS_ES = {
    0: "lunes",
    1: "martes",
    2: "miercoles",
    3: "jueves",
    4: "viernes",
    5: "sabado",
    6: "domingo",
}

MONTHS_ES = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre",
}


class ChatMessage(BaseModel):
    role: str = Field(pattern="^(user|model)$")
    text: str = Field(min_length=1, max_length=6000)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=6000)
    module: str | None = Field(default=None, max_length=80)
    energy: str | None = Field(default=None, max_length=40)
    context: dict | None = None
    history: list[ChatMessage] = Field(default_factory=list, max_length=10)


class ChatResponse(BaseModel):
    reply: str
    model: str = GEMINI_MODEL


def describe_day(dt: datetime) -> dict:
    return {
        "date": dt.date().isoformat(),
        "time": dt.strftime("%H:%M"),
        "weekday": WEEKDAYS_ES[dt.weekday()],
        "month": MONTHS_ES[dt.month],
        "year": dt.year,
        "is_weekend": dt.weekday() >= 5,
        "is_school_day_general": dt.weekday() < 5,
    }


@app.get("/")
def root():
    return {
        "service": "FIACH Time API",
        "status": "ok",
        "docs": "/docs",
        "time_endpoint": "/time",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/time")
def get_time():
    now = datetime.now(TZ)
    tomorrow = now + timedelta(days=1)

    return {
        "timezone": "America/Santiago",
        "current": describe_day(now),
        "tomorrow": describe_day(tomorrow),
        "guidance": {
            "rule": "Usar temporalidad para contextualizar, priorizar y reducir carga docente. No inventar fechas ni horarios."
        },
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request_data: ChatRequest) -> ChatResponse:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY no configurada")
        raise HTTPException(
            status_code=500,
            detail="La API key de Gemini no esta configurada en el servidor.",
        )

    context_lines = []
    if request_data.module:
        context_lines.append(f"Modulo FIACH: {request_data.module}")
    if request_data.energy:
        context_lines.append(f"Energia docente declarada: {request_data.energy}")
    if request_data.context:
        context_lines.append(f"Contexto adicional: {request_data.context}")

    user_text = request_data.message
    if context_lines:
        user_text = "\n".join(context_lines) + "\n\nMensaje docente:\n" + user_text

    contents = [
        {
            "role": item.role,
            "parts": [{"text": item.text}],
        }
        for item in request_data.history[-10:]
    ]
    contents.append({"role": "user", "parts": [{"text": user_text}]})

    payload = {
        "systemInstruction": {"parts": [{"text": FIACH_SYSTEM_PROMPT}]},
        "contents": contents,
        "generationConfig": {
            "temperature": 0.35,
            "topP": 0.9,
            "maxOutputTokens": 900,
        },
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                GEMINI_ENDPOINT,
                params={"key": api_key},
                json=payload,
            )
        response.raise_for_status()
        data = response.json()
        parts = data["candidates"][0]["content"]["parts"]
        reply = "\n".join(part.get("text", "") for part in parts).strip()
        if not reply:
            raise ValueError("Respuesta vacia desde Gemini")
        return ChatResponse(reply=reply)
    except httpx.HTTPStatusError as exc:
        logger.exception("Error Gemini status=%s body=%s", exc.response.status_code, exc.response.text)
        raise HTTPException(
            status_code=502,
            detail="Gemini no pudo responder en este momento.",
        ) from exc
    except Exception as exc:
        logger.exception("Error llamando Gemini")
        raise HTTPException(
            status_code=500,
            detail="No fue posible generar una respuesta FIACH en este momento.",
        ) from exc
