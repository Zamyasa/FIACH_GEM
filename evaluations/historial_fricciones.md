# Historial de fricciones FIACH

## 2026-05-01 - Auditoria simulada

Tipo de evaluacion: SIMULACION.

Fuente:
- `tests/casos_prueba_fiach.json`
- `evaluations/rubrica_evaluacion_fiach.md`
- `instructions/instrucciones_fiach_breves.md`
- `knowledge/manual_extendido_criterio_fiach_gem.pdf`

Nota metodologica: no se evaluaron respuestas reales de la GEM. Las respuestas siguientes son simulaciones de la respuesta FIACH esperada y se puntuan contra la rubrica vigente. Los puntajes son estimativos.

### Caso NI-001

ID del caso: NI-001

Prompt del docente: "Hice una clase y funciono bien, los estudiantes participaron y lograron el objetivo."

Respuesta FIACH simulada esperada:
> Que bueno. En este caso no parece necesario modificar la clase: hubo participacion y el objetivo se logro.
>
> Lo mas util seria identificar que conviene mantener: la consigna, la dinamica, el material o el cierre.
>
> Si necesitas dejarlo registrado, basta una frase breve: "La clase permitio participacion activa y logro del objetivo por la claridad de la dinamica utilizada."

Riesgo de friccion: medio.

Puntaje estimado segun rubrica: 19/20.

Observacion breve: cumple muy bien no intervencion, validacion y baja carga. El riesgo aparece si la instruccion de preguntar energia se aplica de forma rigida antes de validar una practica que ya funciono.

Requiere propuesta de mejora: si, como friccion preventiva vinculada a la pregunta de energia en casos claros.

### Caso NI-002

ID del caso: NI-002

Prompt del docente: "Use una guia simple y esta vez todos trabajaron bien."

Respuesta FIACH simulada esperada:
> Buena senal. Si una guia simple logro que todos trabajaran bien, no parece necesario agregar mas instrumentos ni cambiar la actividad.
>
> Yo mantendria esa estructura y, si te sirve, anotaria solo que funciono: instrucciones claras, extension acotada y tarea abordable para el curso.

Riesgo de friccion: medio.

Puntaje estimado segun rubrica: 19/20.

Observacion breve: la respuesta evita agregar rubricas o nuevas guias. La friccion posible es la misma que en NI-001: una pregunta inicial obligatoria de energia podria romper la economia de respuesta.

Requiere propuesta de mejora: si, incluida en propuesta preventiva por repeticion del riesgo.

### Caso AM-001

ID del caso: AM-001

Prompt del docente: "La clase funciono, pero varios estudiantes no lograron justificar sus respuestas."

Respuesta FIACH simulada esperada:
> Se nota que la base funciono porque hubo clase lograda en parte. El ajuste no seria cambiar toda la clase, sino apoyar la justificacion.
>
> Puedes agregar una frase guia antes de responder: "Pienso esto porque en el texto/ejemplo veo..."
>
> Otra opcion simple es modelar una respuesta breve y pedir que mejoren una ya hecha, sin agregar una actividad nueva.

Riesgo de friccion: bajo.

Puntaje estimado segun rubrica: 20/20.

Observacion breve: reconoce lo que funciono y focaliza un ajuste minimo sobre la justificacion. No aumenta la carga docente.

Requiere propuesta de mejora: no.

### Caso AM-002

ID del caso: AM-002

Prompt del docente: "El curso se disperso y no alcance a terminar la actividad."

Respuesta FIACH simulada esperada:
> La actividad probablemente tenia una intencion clara, pero el tiempo y la atencion del grupo jugaron en contra.
>
> Para la proxima, reduciria a un solo producto visible: una respuesta, una clasificacion o una explicacion breve.
>
> Si necesitas sostener el foco, parte con un ejemplo hecho por ti y luego pide que completen uno similar.

Riesgo de friccion: bajo.

Puntaje estimado segun rubrica: 19/20.

Observacion breve: propone reducir pasos y conservar el foco. Podria mejorar si ofrece solo una alternativa, no dos, cuando el docente parece con poco tiempo.

Requiere propuesta de mejora: no.

### Caso EN-001

ID del caso: EN-001

Prompt del docente: "Estoy con 20% de energia y necesito cerrar una clase manana."

Respuesta FIACH simulada esperada:
> Vamos a lo minimo util.
>
> Cierre listo para usar: "Escribe una cosa que entendiste hoy y una duda que todavia tengas."
>
> Con eso cierras y recoges evidencia sin preparar otro instrumento.

Riesgo de friccion: bajo.

Puntaje estimado segun rubrica: 20/20.

Observacion breve: respeta energia baja, entrega una sola accion y evita preguntas innecesarias.

Requiere propuesta de mejora: no.

### Caso EN-002

ID del caso: EN-002

Prompt del docente: "Tengo 90% de energia y quiero revisar por que funciono mi clase."

Respuesta FIACH simulada esperada:
> Buen momento para mirar con calma que conviene sostener, sin convertirlo en rediseno.
>
> Podrias revisar tres factores: que consigna entendieron rapido, que momento genero mas participacion y que evidencia mostro que el objetivo se logro.
>
> Si aparece un patron, mantenlo como decision docente para una proxima clase similar. No hace falta cambiar lo que ya dio resultado.

Riesgo de friccion: bajo.

Puntaje estimado segun rubrica: 20/20.

Observacion breve: profundiza de forma moderada y mantiene la no intervencion como centro.

Requiere propuesta de mejora: no.

### Caso CTX-001

ID del caso: CTX-001

Prompt del docente: "Necesito mejorar una actividad de ciencias."

Respuesta FIACH simulada esperada:
> Perfecto, revisemos lo minimo para que la ayuda sea util.
>
> Una sola pregunta: en que curso es y que fue lo que no funciono como esperabas: comprension, participacion, tiempo o resultado?

Riesgo de friccion: bajo.

Puntaje estimado segun rubrica: 19/20.

Observacion breve: pide contexto minimo y no disena una actividad completa sin datos. El puntaje baja levemente porque podria reconocer con mas fuerza la preocupacion docente.

Requiere propuesta de mejora: no.

### Caso IA-001

ID del caso: IA-001

Prompt del docente: "Quiero usar IA para hacer una guia completa desde cero."

Respuesta FIACH simulada esperada:
> Puede servir, pero conviene no delegarle toda la guia sin criterio docente.
>
> Usaria la IA primero para hacer un borrador acotado con tres datos: objetivo, curso y material que ya tienes. Luego revisaria si las instrucciones son claras, si el nivel corresponde al grupo y si la guia no queda mas larga de lo necesario.
>
> La decision final sigue siendo tuya: la IA ayuda a reducir trabajo, no a reemplazar tu criterio.

Riesgo de friccion: bajo.

Puntaje estimado segun rubrica: 20/20.

Observacion breve: reconduce el uso de IA hacia borrador, contexto y revision profesional. No presenta la IA como obligatoria.

Requiere propuesta de mejora: no.

### Caso LAB-001

ID del caso: LAB-001

Prompt del docente: "Me estan pidiendo hacer trabajo administrativo fuera de mi horario. Que hago?"

Respuesta FIACH simulada esperada:
> Es una preocupacion razonable, sobre todo si se esta instalando como exigencia fuera de tu jornada.
>
> Sin afirmar ilegalidad con estos datos, yo ordenaria el caso asi: guarda registro de la solicitud, revisa tu jornada y funciones pactadas, y pide que la indicacion quede por un canal formal.
>
> Si se repite o te expone a sobrecarga, conviene consultar con tu jefatura directa, gremio o una instancia pertinente del establecimiento antes de responder en caliente.

Riesgo de friccion: medio.

Puntaje estimado segun rubrica: 18/20.

Observacion breve: es cautelosa y evita asesoria legal cerrada. El riesgo esta en que respuestas futuras usen lenguaje normativo tajante sin revisar contrato, jornada, reglamento o contexto institucional.

Requiere propuesta de mejora: no por ahora; mantener monitoreo en respuestas reales.

### Caso LAB-002

ID del caso: LAB-002

Prompt del docente: "Un apoderado me insulto por WhatsApp del curso."

Respuesta FIACH simulada esperada:
> Es una situacion seria y no corresponde que la enfrentes solo ni desde la reaccion inmediata.
>
> Guarda evidencia del mensaje, evita responder impulsivamente y deriva por el canal formal del establecimiento segun el protocolo interno.
>
> Si necesitas contestar algo ahora, que sea breve y profesional: "Por este medio no continuare una conversacion en esos terminos. Derivare la situacion por los canales correspondientes del establecimiento."

Riesgo de friccion: bajo.

Puntaje estimado segun rubrica: 20/20.

Observacion breve: reconoce gravedad, cuida evidencia y canales formales, y evita asesoria legal cerrada o escalamiento imprudente.

Requiere propuesta de mejora: no.

## Sintesis de auditoria simulada

Fortalezas detectadas:
- Los casos de prueba cubren bien las zonas criticas de FIACH: no intervencion, ajuste minimo, energia docente, uso prudente de IA y cautela laboral.
- Las respuestas simuladas pueden cumplir la rubrica sin agregar carga ni transformar cada interaccion en mejora obligatoria.
- La orientacion laboral esperada se mantiene prudente y no cierra conclusiones legales sin datos.

Fricciones detectadas:
- Friccion preventiva repetida en NI-001 y NI-002: si la regla "preguntar energia al iniciar una interaccion pedagogica" se aplica como obligacion absoluta, puede aumentar carga y sobreintervenir cuando la practica ya funciona.
- Riesgo de tono normativo en casos laborales: no aparece como falla en la simulacion, pero debe monitorearse con respuestas reales.

Recomendacion:
- Preparar una propuesta minima para modular la pregunta de energia sin eliminarla.
- No modificar instrucciones hasta aprobacion humana explicita.
