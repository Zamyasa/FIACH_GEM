# Prompt para automatización en Codex

Cada viernes, ejecuta una auditoría FIACH sobre los casos de prueba del repositorio.

Tareas:
1. Lee /instructions/instrucciones_fiach_breves.md y /knowledge/README.md.
2. Revisa /tests/casos_prueba_fiach.json.
3. Evalúa si las respuestas reales disponibles cumplen la rúbrica de /evaluations/rubrica_evaluacion_fiach.md.
4. Si no hay respuestas reales, genera respuestas simuladas marcadas como SIMULACIÓN y evalúalas con cautela.
5. Detecta fricciones, especialmente sobreintervención, exceso de preguntas, aumento de carga, rigidez o falta de cautela laboral.
6. Registra hallazgos en /evaluations/historial_fricciones.md.
7. Si una fricción se repite o es grave, propone actualización mínima en /proposals/propuestas_actualizacion.md.
8. No modifiques instrucciones sin aprobación humana explícita.
9. Si no hay hallazgos relevantes, informa “sin fricciones críticas detectadas”.

Antes de proponer cualquier cambio, verifica:
¿Este cambio mejora FIACH sin volverlo más rígido, más largo o más demandante para el docente?
