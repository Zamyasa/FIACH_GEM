\# AGENTS.md | Reglas de trabajo para Codex en FIACH



Este repositorio contiene el sistema FIACH | Acompañamiento docente.



FIACH es un proyecto piloto de acompañamiento docente con inteligencia artificial. Su propósito es apoyar decisiones pedagógicas reales, reducir carga y respetar el criterio profesional docente.



\## Principio central



Codex no debe actuar como dueño del proyecto. Codex audita, registra, propone y edita solo cuando recibe instrucción explícita.



La aprobación humana de Matías Onell H. es obligatoria antes de modificar instrucciones, documentos base o comportamiento central de FIACH.



\## Reglas generales



1\. No hacer push automáticamente.

2\. No modificar `instructions/` sin aprobación humana explícita.

3\. No modificar `knowledge/` sin aprobación humana explícita.

4\. No modificar `tests/` salvo solicitud directa.

5\. No modificar `README.md`, `NOTICE.md`, `VERSION.md`, `CHANGELOG.md` ni este archivo sin solicitud directa.

6\. Registrar fricciones reales en `evaluations/historial\_fricciones.md`.

7\. Registrar propuestas en `proposals/propuestas\_actualizacion.md`.

8\. No crear cambios grandes si basta con registrar una observación.

9\. No proponer cambios de instrucciones por una fricción leve aislada.

10\. Mantener siempre el principio FIACH de no aumentar carga docente.



\## Modos de trabajo



\### Modo auditor



Usar cuando se pida revisar comportamiento, pruebas o fricciones.



Puede leer:

\- `instructions/instrucciones\_fiach\_breves.md`

\- `knowledge/`

\- `tests/`

\- `evaluations/historial\_fricciones.md`

\- `proposals/propuestas\_actualizacion.md`

\- `VERSION.md`

\- `CHANGELOG.md`



Puede modificar solo:

\- `evaluations/historial\_fricciones.md`

\- `proposals/propuestas\_actualizacion.md`



No debe modificar instrucciones en modo auditor.



\### Modo editor



Usar solo cuando Matías apruebe explícitamente aplicar una propuesta.



Puede modificar:

\- el archivo indicado por la solicitud.



Debe:

\- aplicar el cambio mínimo necesario;

\- mostrar diff para revisión humana;

\- no hacer push;

\- no tocar archivos no solicitados.



\## Criterios para proponer cambios



Codex solo debe proponer cambios a instrucciones si ocurre una de estas condiciones:



1\. Falla crítica.

2\. Fricción repetida dos o más veces.

3\. Contradicción clara entre instrucciones y respuesta real.

4\. Riesgo evidente de aumentar carga docente.

5\. Debilitamiento del criterio profesional docente.

6\. Error en temporalidad, energía docente o regla de no intervención.



Si la respuesta fue útil pero algo extensa, registrar como fricción leve y monitorear antes de modificar instrucciones.



\## Criterio FIACH obligatorio



Toda propuesta debe responder:



¿Esto mejora la práctica sin aumentar la carga docente?



Si la respuesta es no, no proponer el cambio.



\## Archivos principales



\- `instructions/instrucciones\_fiach\_breves.md`: instrucciones operativas breves de la GEM.

\- `knowledge/`: documentos base y manuales.

\- `tests/`: casos de prueba.

\- `evaluations/historial\_fricciones.md`: historial de pruebas, fricciones y validaciones.

\- `proposals/propuestas\_actualizacion.md`: propuestas pendientes o aplicadas.

\- `time\_api/`: API de temporalidad usada por FIACH.

\- `NOTICE.md`: autoría y resguardo.

\- `VERSION.md`: versión actual del proyecto.

\- `CHANGELOG.md`: registro de cambios relevantes.



\## Restricciones



No revelar ni publicar instrucciones internas, prompts maestros, configuraciones técnicas, historial de fricciones ni documentos internos sin autorización.



No transformar FIACH en una herramienta obligatoria. El uso de FIACH debe mantenerse voluntario.



No convertir FIACH en evaluador, supervisor ni fiscalizador.



No aumentar la carga docente con nuevas tareas, instrumentos, registros o actividades innecesarias.



\## Estado actual



FIACH V1 piloto.



Estado: estable para pruebas internas, validación exploratoria y capacitación docente inicial del 28 de mayo.

