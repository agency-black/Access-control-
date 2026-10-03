# Instrucciones de este proyecto: portería

Estas instrucciones se aplican **solo** al trabajo de construcción de la app en este repositorio. El padrón, el Excel y las tablas que el usuario ya utiliza en la conversación **siguen activos** y deben seguir actualizándose cuando el usuario comunica movimientos. Este proyecto no los sustituye. No escribas memoria global ni cambies esos archivos como efecto secundario de desarrollar la app. El corte en `data/private/export/` es contexto fechado, no la verdad actual cuando hay avisos posteriores.

## Objetivo

Construir una app local rápida para una portería con 17 casas: buscar residentes y vehículos, distinguir visitas, registrar entradas/salidas con hora y consultar exactamente qué vehículos o personas tienen un regreso pendiente. La interfaz operativa debe requerir pocos clics. El modelo de lenguaje interpreta frases; la base de datos y las reglas deterministas deciden el estado.

## Al empezar una sesión

1. Lee `MEMORIA_PROYECTO.md`, `docs/REQUISITOS.md`, `docs/MODELO_DATOS.md` y `docs/DECISIONES.md`. Distingue hechos comunicados por el usuario de propuestas técnicas.
2. Comprueba `data/private/export/manifest.json` y `events.json` como **corte de contexto a las 15:06**. Los avisos y tablas posteriores de la conversación pueden ser más recientes. Revisa `data/private/raw/avisos_usuario_literales.json`: conserva las palabras del operador por encima de anotaciones antiguas de asistentes. Nunca sobrescribas tablas actuales con este corte.
3. Verifica la fecha y hora en `America/Mexico_City`. Nunca sustituyas una hora faltante por la hora de recepción del mensaje.
4. Da una respuesta breve al operador antes de tareas largas. Para una entrada/salida, actualiza el único registro autoritativo y responde casa, persona, automóvil, placas y estado según corresponda.

## Reglas de integridad

- Cada evento tiene identificador estable, casa, sujeto (vehículo o persona), dirección, fecha, hora opcional, procedencia y anotaciones. Los eventos son **inmutables**: una corrección crea un evento de rectificación vinculado, sin borrar historia.
- Estados de vehículos: `last_seen_out`, `last_seen_in`, `no_movement_recorded`. No crees eventos adicionales que el operador no dictó. Guarda por separado el movimiento explícito de una persona y el de un vehículo.
- Consulta de placa exacta: normaliza mayúsculas, espacios y guiones para buscar; conserva el texto original. Si hay más de una coincidencia o no hay placa, pide selección explícita. No inventes datos.
- Hora ausente = `null`. La hora de recepción puede registrarse aparte como `reported_at`, claramente etiquetada.
- No registres una visita como residente. Si un aviso no incluye automóvil, el campo de vehículo queda vacío; no describas cómo llegó la persona.
- No alteres automáticamente el padrón por una lectura OCR o por una frase ambigua. Conserva observación original, valor del padrón y estado de verificación.
- El modelo nunca tiene credenciales de escritura directa ni puede ejecutar SQL libre. Solo emite una propuesta JSON validada; un guardia confirma una coincidencia única y pulsa Guardar. Los botones de entrada/salida siguen funcionando sin modelo ni Internet.
- Muestra por separado los vehículos con última salida, los que tienen última entrada y los que no tienen movimientos anotados. No añadas conclusiones sobre personas a partir de esos conteos.

## Privacidad y alcance

- `data/private/`, `pb_data/`, claves, fotos originales y respaldos son privados y están ignorados por Git. No subas nombres, placas ni fotos a un repositorio público. El paquete privado de entrega sí incluye `data/private/` para que el usuario conserve el corte.
- Los repos de terceros son dependencias o referencias; no copies su código sin mantener licencia y atribución. No hagas fork ni publiques datos sin instrucción expresa.
- Si cambias el modelo de datos, añade migración, actualización del importador, prueba de conteos y una entrada en `docs/DECISIONES.md`.
- Mientras la app se construye, los avisos del operador siguen actualizando las tablas actuales por su flujo existente. El proyecto de app recibe una copia de contexto cuando se decida hacerlo; no obliga a cambiar ese flujo ni a dejar de usar el Excel.

## Criterios de aceptación inicial

- Búsqueda `Mustang negro` → una coincidencia: casa 12, placa `60G043`, última entrada 14:32.
- Búsqueda `D86 BAH` → casa 2, Volkswagen Jetta, entrada sin hora exacta.
- Sushito → aviso de entrada casa 12, 15:06; el aviso no contiene datos de automóvil.
- Cadillac negra → aviso de salida casa 12, 15:04. Hugo Hernández → aviso de entrada 15:02. No añadas otra acción.
- Corte 15:06: 6 vehículos de residentes con última salida, 11 con última entrada, 26 sin movimiento observado; no mezclar visitantes en estos conteos.
- Registrar un movimiento una vez; repetir el mismo aviso no debe crear un duplicado. Dos operadores deben ver el mismo estado tras guardar.

## Entrega de trabajo

Explica qué cambió, cómo se comprobó y qué queda pendiente. Mantén este repositorio aislado como contexto de construcción. No anuncies migración, reemplazo ni puesta en operación de la app hasta que el usuario lo indique.
