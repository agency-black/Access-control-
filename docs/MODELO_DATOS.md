# Modelo de datos y migración

La carpeta `data/private/export/` es un corte de contexto normalizado. Sus archivos son JSON UTF-8 y llevan identificadores estables. Las tablas actuales fuera del proyecto siguen en uso. PocketBase es un candidato para el prototipo; no sobrescribir jamás las tablas actuales con este corte.

| Entidad | Campos principales | Regla |
|---|---|---|
| `houses` | `house_id` 1–17, `residents_label` | Etiqueta combinada del padrón; no dividir nombres por intuición. |
| `vehicles` | `vehicle_id`, casa, clase, modelo, placa original/normalizada, color, tipo | Placa puede faltar en visitas; `vehicle_id` estable, no usar placa como llave. |
| `visitors` | `visitor_id`, nombre anotado, casa, vehículo opcional | Hugo y Sushito son personas, separadas de la Cadillac. |
| `events` | ID, casa, fecha, hora opcional, sujeto, dirección, fuente, nota, autor, `reported_at` | Append-only. `subject_type` = vehículo o persona. |
| `corrections` | ID, evento original, nuevo valor, causa, operador, fecha | Corrige sin eliminar evidencia original. |
| `aliases/observations` | placa foto, placa padrón, estado de verificación, fuente | Conserva desacuerdos sin sobreescribir la verdad. |

## Estado derivado

Ordenar eventos por secuencia de confirmación y fecha/hora cuando existe. Para cada vehículo, el último evento relevante define `last_seen_in` o `last_seen_out`; sin evento = `no_movement_recorded`. Guardar únicamente los eventos de persona y automóvil comunicados expresamente. Un evento sin hora exacta mantiene `time = null` y `reported_at` en otra columna.

## Hechos de la importación

- 17 casas, 43 autos de residentes, 4 vehículos de visita preexistentes, una Cadillac visitante.
- 31 eventos; último evento: Sushito entra a casa 12, 15:06.
- El aviso de Sushito se exporta como entrada de persona a las 15:06; no se agrega automóvil porque el aviso no lo menciona.
- El aviso de las 15:04 registra únicamente la salida de la Cadillac. No crear otro evento.
- Entrada del Jetta y la “E” de Cynthia carecen de hora exacta.

## Importación idempotente propuesta si se adopta PocketBase

1. Crear colecciones mediante migraciones versionadas. Restringir `events` a escritura por una ruta de dominio; bloquear `updateRule`/`deleteRule` ordinarios.
2. Importar casas/vehículos/visitantes por sus IDs de fuente; nunca duplicar al reintentar.
3. Importar cada evento con `event_id = legacy-20261003-NNN`. Reintento con mismo ID = sin cambio; payload distinto = conflicto que se revisa.
4. Validar conteos y casos de aceptación. Mantener el manifiesto SHA-256 de los archivos fuente.
5. Si ya hay eventos nuevos en PocketBase, no reemplazar ni reiniciar la base; respaldar antes de cualquier migración.

## Reglas de consulta

La normalización para búsqueda quita espacios, guiones, acentos y cambia a mayúsculas, pero conserva `plate_display`. Consulta por descripción puede devolver varias coincidencias. `No anotadas` nunca cuenta como placa única. Las fotografías de autos del padrón son referencias genéricas; no prueban identidad de un vehículo que llega.
