# Propuestas de actualizacion FIACH

Toda propuesta debe incluir:

1. Friccion detectada.
2. Evidencia del caso de prueba.
3. Archivo a modificar.
4. Bloque actual.
5. Bloque propuesto.
6. Justificacion pedagogica.
7. Riesgo del cambio.
8. Recomendacion: aprobar / ajustar / rechazar.

No aplicar cambios sin aprobacion humana explicita.

## 2026-05-01 - Propuesta preventiva sobre energia docente

Estado: aplicada; friccion resuelta en revision humana para caso "clase que funciono bien".

### 1. Friccion detectada

La instruccion actual indica preguntar por la energia docente al iniciar una interaccion pedagogica. Aplicada de forma rigida, puede generar sobreintervencion en casos donde la practica ya funciona o donde el docente ya entrego suficiente contexto para responder con validacion breve.

### 2. Evidencia del caso de prueba

Casos relacionados:
- NI-001: "Hice una clase y funciono bien, los estudiantes participaron y lograron el objetivo."
- NI-002: "Use una guia simple y esta vez todos trabajaron bien."

En ambos casos, el esperado exige reconocer, validar y no agregar pasos. Una pregunta inicial obligatoria sobre energia podria sentirse como una carga adicional o desviar una respuesta que debe ser breve.

### 3. Archivo a modificar

`instructions/instrucciones_fiach_breves.md`

No se modifica en esta auditoria. Solo se propone para revision.

### 4. Bloque actual

Seccion 6. Energia docente:

> Al iniciar una interaccion pedagogica, pregunta: "Con cuanta energia estas hoy para esto? (10%-100%)"
>
> La energia regula profundidad, extension y exigencia, no calidad. No la uses para exigir mas trabajo.

### 5. Bloque propuesto

> Al iniciar una interaccion pedagogica, pregunta por la energia docente solo si ayuda a ajustar la profundidad de la respuesta y no agrega carga innecesaria.
>
> Si el docente ya declara su energia, usala directamente.
>
> Si la situacion es clara, urgente o la practica ya funciono, puedes responder sin preguntar energia y mantener una ayuda breve, cuidadosa y aplicable.
>
> La energia regula profundidad, extension y exigencia, no calidad. No la uses para exigir mas trabajo.

### 6. Justificacion pedagogica

El cambio conserva el principio de energia docente, pero evita que se convierta en un paso mecanico. Refuerza la no intervencion cuando una practica ya funciono y reduce la posibilidad de agregar carga conversacional innecesaria.

### 7. Riesgo del cambio

Riesgo bajo a medio: si se flexibiliza demasiado, la GEM podria omitir la energia en situaciones donde si seria util. Para mitigarlo, el bloque propuesto mantiene la pregunta cuando ayuda a regular profundidad y extension.

### 8. Recomendacion

Ajustar antes de aprobar: validar con respuestas reales o una segunda bateria simulada si esta flexibilizacion mejora NI-001, NI-002 y EN-001 sin debilitar el criterio de energia docente.

### 9. Seguimiento

Revision humana posterior:
- Fecha: 2026-05-01.
- Caso: clase que funciono bien.
- Resultado: aprobado.
- Observacion: FIACH reconocio la practica, no sobreintervino y no pregunto energia.
- Estado: friccion resuelta.

## 2026-05-02 - Propuesta minima sobre baja energia 10%-40%

Estado: pendiente de revision humana.

### 1. Friccion detectada

En energia declarada baja, FIACH puede sobreestructurar la respuesta si transforma una necesidad puntual en una clase completa. Esto aumenta carga docente y contradice el criterio de entregar una ayuda minima, lista para usar.

### 2. Evidencia del caso de prueba

Caso relacionado:
- EN-001: "Estoy con 20% de energia y necesito cerrar una clase manana."

Resultado real observado:
- Evaluacion: no aprobado.
- FIACH reconocio la baja energia, pero genero objetivo, inicio, desarrollo, cierre, ticket de salida, registro para planificacion y version alternativa.
- La respuesta fue pedagogicamente coherente, pero demasiado extensa para 20% de energia.

### 3. Archivo a modificar

`instructions/instrucciones_fiach_breves.md`

No se modifica en esta accion. Solo se propone para revision.

### 4. Bloque actual

Seccion 6. Energia docente:

> 10%-40%: una accion breve. Si funciona, reconoce y deja una frase lista solo si sirve.

### 5. Bloque propuesto

> 10%-40%: entrega solo una accion simple o un cierre minimo viable, listo para usar. No planifiques una clase completa, no agregues multiples componentes y no ofrezcas versiones alternativas salvo que el docente las pida.

### 6. Justificacion pedagogica

El caso EN-001 muestra que "una accion breve" puede no bastar para impedir que FIACH agregue estructura excesiva. La formulacion propuesta explicita el limite operativo: una sola accion o cierre minimo viable, sin clase completa ni capas adicionales.

### 7. Riesgo del cambio

Riesgo bajo: podria volver demasiado escueta alguna respuesta de baja energia. Se mitiga porque el bloque permite una accion simple lista para usar y el docente siempre puede pedir ampliar.

### 8. Recomendacion

Aprobar con revision humana si se confirma que mejora EN-001 sin reducir la utilidad de respuestas breves en baja energia.

## 2026-05-02 - Propuesta minima sobre cruce temporal y contexto escolar

Estado: pendiente de revision humana.

### 1. Friccion detectada

Temporalidad parcial repetida: FIACH usa referencias como "manana" o "esta semana" para priorizar y reducir carga, pero no siempre cruza esa referencia con el dia actual, calendario disponible y contexto escolar real.

### 2. Evidencia del caso de prueba

Casos relacionados:
- TEMP-002: FIACH uso "manana" para priorizar, pero no verifico que manana correspondia a domingo.
- TEMP-003: "Manana tengo que dejar lista una guia para mi curso, pero estoy con poco tiempo. Que hago?"

Resultado real observado en TEMP-003:
- Evaluacion: aprobado con ajuste menor.
- FIACH propuso una guia minima viable con objetivo, 3 actividades y cierre breve.
- La respuesta fue util y redujo carga, pero no aclaro la posible inconsistencia de "manana" si era domingo.

### 3. Archivo a modificar

`instructions/instrucciones_fiach_breves.md`

No se modifica en esta accion. Solo se propone para revision.

### 4. Bloque actual

Seccion 5. Contexto minimo:

> Temporalidad FIACH: usa fecha, hora, dia actual o calendario disponible para contextualizar, priorizar y reducir carga. No inventes fechas ni horarios; si son clave y faltan, pregunta lo minimo. No crees, muevas ni elimines eventos sin confirmacion explicita.

### 5. Bloque propuesto

> Temporalidad FIACH: usa fecha, hora, dia actual o calendario disponible para contextualizar, priorizar y reducir carga. Cruza referencias como hoy, manana o esta semana con el dia actual y el contexto escolar. No inventes fechas ni horarios; si hay inconsistencia o faltan datos clave, aclaralo en una frase y sigue con una ayuda minima. No crees, muevas ni elimines eventos sin confirmacion explicita.

### 6. Justificacion pedagogica

La propuesta mantiene la ayuda activa y evita detener el trabajo, pero mejora la contextualizacion temporal. En contexto docente, "manana" puede no equivaler al proximo dia laboral; aclararlo brevemente reduce errores y carga sin convertir la respuesta en interrogatorio.

### 7. Riesgo del cambio

Riesgo bajo a medio: FIACH podria sobreexplicar el calendario o preguntar de mas. Se mitiga indicando que la aclaracion debe ser una frase y que la ayuda minima debe continuar.

### 8. Recomendacion

Aprobar si se confirma que mejora TEMP-002 y TEMP-003 sin aumentar la carga ni frenar la respuesta.
