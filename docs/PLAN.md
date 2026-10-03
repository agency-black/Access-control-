# Construcción por incrementos verificables

## 0. Corte e aislamiento — completado

Proyecto aislado, `AGENTS.md`, memoria, exportación privada, fotos y Excel de referencia; validación de 17/43/31 y casos recientes. El repositorio local no tiene remoto.

## 1. Motor de datos — siguiente

- Fijar versión PocketBase y crear migraciones `houses`, `vehicles`, `visitors`, `events`, `corrections`, `operators` con reglas de acceso.
- Importador idempotente de `data/private/export/`, con respaldo y validación de manifiesto.
- Ruta para registrar un evento en una transacción y consultar estado derivado; `client_event_id` único y correcciones auditadas.
- Pruebas de 6/11/26, Cadillac/Hugo y Sushito sin vehículo.

**Salida:** API local con consultas y captura correctas, sin modelo.

## 2. Interfaz de portería

- Vue/Vite: búsqueda grande, tarjetas de seis pendientes, visitas, registro de entrada/salida y confirmación.
- Casa y placa visibles en toda búsqueda y cada movimiento. Filtro por modelo/color/persona/placa.
- Realtime para dos navegadores; error claro si hay ambigüedad o conexión caída.

**Salida:** operador usa la app sin terminal ni Excel.

## 3. Lenguaje natural y fotos

- Ruta de servidor hacia Ollama, esquema JSON, clave solo servidor, propuesta revisable.
- Medir latencia y errores con frases de aceptación: “ya llegó el Jetta”, “se fue la Cadillac”, “entró Sushito casa 12”, “Mustang negro”.
- OCR de fotos como sugerencia con valores originales, sin importación automática.

**Salida:** dictado acelera captura; botones manuales permanecen.

## 4. Operación y exportación

- Exportación XLSX/CSV bajo demanda desde DB; respaldo, restauración y guía de instalación Mac.
- Prueba de cambio de turno y de caída de Internet. No publicar padrón en repositorio remoto.

**Salida:** app instalada para uso diario y una sola fuente operativa.
