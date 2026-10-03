# Construcción por incrementos verificables

## 0. Contexto y aislamiento — completado

Proyecto aislado, `AGENTS.md`, memoria, copias privadas, fotos y Excel de referencia; validación de 17/43/31 y casos recientes. El repositorio local no tiene remoto. **Las tablas actuales continúan utilizándose fuera de este proyecto.**

## 1. Prototipo del motor de datos — siguiente

- Evaluar PocketBase y fijar versión si se adopta. Crear un prototipo de `houses`, `vehicles`, `visitors`, `events`, `corrections`, `operators` con reglas de acceso.
- Importador idempotente de `data/private/export/`, con respaldo y validación de manifiesto.
- Ruta para registrar un evento en una transacción y consultar estado derivado; `client_event_id` único y correcciones auditadas.
- Pruebas de 6/11/26 y de las tres anotaciones explícitas: entrada de Hugo, salida de Cadillac y entrada de Sushito.

**Salida:** API de prueba con consultas y captura correctas sobre copias, sin modificar las tablas existentes.

## 2. Interfaz de portería

- Vue/Vite: búsqueda grande, tarjetas de seis pendientes, visitas, registro de entrada/salida y confirmación.
- Casa y placa visibles en toda búsqueda y cada movimiento. Filtro por modelo/color/persona/placa.
- Realtime para dos navegadores; error claro si hay ambigüedad o conexión caída.

**Salida:** interfaz de prueba utilizable; el operador sigue usando las tablas actuales hasta acordar un cambio.

## 3. Lenguaje natural y fotos

- Ruta de servidor hacia Ollama, esquema JSON, clave solo servidor, propuesta revisable.
- Medir latencia y errores con frases de aceptación: “ya llegó el Jetta”, “se fue la Cadillac”, “entró Sushito casa 12”, “Mustang negro”.
- OCR de fotos como sugerencia con valores originales, sin importación automática.

**Salida:** dictado acelera captura; botones manuales permanecen.

## 4. Evaluación de operación y exportación

- Exportación XLSX/CSV bajo demanda desde DB; respaldo, restauración y guía de instalación Mac.
- Prueba de cambio de turno y de caída de Internet. No publicar padrón en repositorio remoto.

**Salida:** app evaluada con el operador. La decisión de usarla para el turno, integrarla con el Excel o migrar datos queda pendiente de instrucciones explícitas.
