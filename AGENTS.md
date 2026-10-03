# Instrucciones de este proyecto: portería

Estas instrucciones se aplican **solo** a este repositorio. No escribas memoria global, no edites archivos del directorio padre y no uses otras conversaciones como fuente de verdad si contradicen `data/private/export/` o los movimientos nuevos confirmados por el operador.

## Objetivo

Construir una app local rápida para una portería con 17 casas: buscar residentes y vehículos, distinguir visitas, registrar entradas/salidas con hora y consultar exactamente qué vehículos o personas tienen un regreso pendiente. La interfaz operativa debe requerir pocos clics. El modelo de lenguaje interpreta frases; la base de datos y las reglas deterministas deciden el estado.

## Al empezar una sesión

1. Lee `MEMORIA_PROYECTO.md`, `docs/REQUISITOS.md`, `docs/MODELO_DATOS.md` y `docs/DECISIONES.md`.
2. Comprueba `data/private/export/manifest.json`, la última secuencia de `events.json` y los datos operativos más recientes de la base de datos si ya existe. El JSON es un **corte inicial**, no una fuente que deba sobrescribir movimientos posteriores.
3. Verifica la fecha y hora en `America/Mexico_City`. Nunca sustituyas una hora faltante por la hora de recepción del mensaje.
4. Da una respuesta breve al operador antes de tareas largas. Para una entrada/salida, actualiza el único registro autoritativo y responde casa, persona, automóvil, placas y estado según corresponda.

## Reglas de integridad

- Cada evento tiene identificador estable, casa, sujeto (vehículo o persona), dirección, fecha, hora opcional, procedencia y anotaciones. Los eventos son **inmutables**: una corrección crea un evento de rectificación vinculado, sin borrar historia.
- Estados: `last_seen_out`, `last_seen_in`, `no_movement_recorded`, `unknown`. Una salida de vehículo no prueba que su conductor o titular haya salido. Una entrada de vehículo no prueba que todos los residentes de esa casa estén dentro.
- Consulta de placa exacta: normaliza mayúsculas, espacios y guiones para buscar; conserva el texto original. Si hay más de una coincidencia o no hay placa, pide selección explícita. No inventes datos.
- Hora ausente = `null`. La hora de recepción puede registrarse aparte como `reported_at`, claramente etiquetada.
- No registres una visita como residente. Una persona sin automóvil identificado debe poder entrar y salir sin crear un automóvil ficticio.
- No alteres automáticamente el padrón por una lectura OCR o por una frase ambigua. Conserva observación original, valor del padrón y estado de verificación.
- El modelo nunca tiene credenciales de escritura directa ni puede ejecutar SQL libre. Solo emite una propuesta JSON validada; un guardia confirma una coincidencia única y pulsa Guardar. Los botones de entrada/salida siguen funcionando sin modelo ni Internet.
- No declares “ya no falta nadie” mientras existan estados `no_movement_recorded` o personas cuya presencia no se haya confirmado. Muestra por separado los vehículos con última salida, los que tienen última entrada y los no observados.

## Privacidad y alcance

- `data/private/`, `pb_data/`, claves, fotos originales y respaldos son privados y están ignorados por Git. No subas nombres, placas ni fotos a un repositorio público. El paquete privado de entrega sí incluye `data/private/` para que el usuario conserve el corte.
- Los repos de terceros son dependencias o referencias; no copies su código sin mantener licencia y atribución. No hagas fork ni publiques datos sin instrucción expresa.
- Si cambias el modelo de datos, añade migración, actualización del importador, prueba de conteos y una entrada en `docs/DECISIONES.md`.
- Si cambia un movimiento del día, actualiza la base operativa; no generes un DOCX ni otro XLSX por evento. Excel es exportación/consulta, no fuente paralela.

## Criterios de aceptación inicial

- Búsqueda `Mustang negro` → una coincidencia: casa 12, placa `60G043`, última entrada 14:32.
- Búsqueda `D86 BAH` → casa 2, Volkswagen Jetta, entrada sin hora exacta.
- Visita Sushito → casa 12, entrada 15:06, `vehicle_id = null`.
- Cadillac → casa 12, última salida 15:04; la presencia de Hugo queda desconocida.
- Corte 15:06: 6 vehículos de residentes con última salida, 11 con última entrada, 26 sin movimiento observado; no mezclar visitantes en estos conteos.
- Registrar un movimiento una vez; repetir el mismo aviso no debe crear un duplicado. Dos operadores deben ver el mismo estado tras guardar.

## Entrega de trabajo

Explica qué cambió, cómo se comprobó y qué queda pendiente. Conserva una sola base de datos autoritativa y un repositorio aislado. Cualquier archivo de exportación lleva fecha de corte y no suplanta el estado en vivo.
