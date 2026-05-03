from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from fastapi import FastAPI

app = FastAPI(
    title="FIACH Time API",
    version="1.0.0",
    description="API simple para entregar fecha, hora y dia actual en zona horaria de Chile.",
)

TZ = ZoneInfo("America/Santiago")

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