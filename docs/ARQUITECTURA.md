# Arquitectura del primer producto

```mermaid
flowchart LR
  A[Operador] --> B[Interfaz Vue]
  B --> C[Rutas de dominio PocketBase]
  C --> D[(SQLite eventos y padrón)]
  C --> E[Ollama Cloud opcional]
  D --> B
```

## Componentes

**PocketBase:** proceso único en la computadora de la portería o un equipo local central. Proporciona SQLite, autenticación, API REST, panel administrativo y suscripciones en tiempo real. Pin a una versión concreta y guarda `pb_migrations/` y `pb_hooks/` en Git; `pb_data/` queda privado. PocketBase recomienda una SPA para el frontend y extensiones para validación de servidor. Su serie anterior a 1.0 puede cambiar, por eso se prueba cualquier actualización. Repositorio: https://github.com/pocketbase/pocketbase

**Vue 3 + Vite + SDK oficial:** PWA o navegador para uso diario. El operador ve casa y placa sin entrar al panel de administración. Una sola pantalla de búsqueda/captura con pestañas de pendientes, visitas e historial. Repositorios: https://github.com/vuejs/core, https://github.com/vitejs/vite, https://github.com/pocketbase/js-sdk

**Ruta de dominio:** validar coincidencia única, casa, sujeto, estado previo, horario y `client_event_id`; escribir el evento y devolver estado derivado. La interfaz no cambia directamente los campos de estado. Las reglas API impiden actualizaciones o borrados arbitrarios del historial. Para varias estaciones, usar una instancia PocketBase compartida y realtime.

**Intérprete opcional:** texto/frase → JSON estructurado `{accion, tipo_sujeto, nombre, placa, modelo, color, casa, hora}`. Un servidor llama a Ollama Cloud con clave en entorno; el navegador nunca recibe la clave. La respuesta se cruza con el padrón y se muestra como propuesta para revisar. PocketBase JSVM tiene `$http.send` para llamadas externas; comprobar su manejo de secretos/errores antes de integrarlo. El fallback determinista siempre queda disponible.

## Estados y tiempo

Los registros de estado son **vistas derivadas** de eventos, no columnas editadas a mano. La hora de observación puede ser nula; `reported_at` se guarda cuando llega el aviso. El orden de incorporación de eventos es estable. Si un evento tardío tiene hora anterior, una rectificación o reconciliación explícita decide el último estado; no ordenar sin contexto para reescribir el historial.

## Backups y operación

Respaldo de `pb_data/` con procedimiento de PocketBase y prueba de restauración antes de abrir la app a otros operadores. Exportación XLSX solo bajo demanda desde la DB, siempre con fecha de corte. El XLSX del 3 de octubre se conserva como referencia de importación; no se sincroniza en paralelo.

## Límites conscientes

La app inicial usa una instancia única; no requiere Docker ni un servicio SaaS de base de datos. Ollama Cloud requiere Internet/clave y envía el texto dictado al proveedor. Las consultas/captura manual operan sin él. No usar imágenes de referencia de internet para reconocer placas reales.
