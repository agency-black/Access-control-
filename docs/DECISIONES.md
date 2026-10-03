# Decisiones y cuestiones abiertas

## Decisión confirmada · 2026-10-03 · Proyecto separado

**Confirmado por el usuario:** este proyecto existe para dar contexto a la construcción de la app. Las tablas y el Excel que ya se usan **no se abandonan ni se alteran por crear este proyecto**. Se siguen actualizando en la conversación. Una eventual migración o sincronización no está decidida.

## Propuesta técnica · 2026-10-03 · Modelo como intérprete

**Por evaluar:** Ollama Cloud con salida JSON estructurada, validación determinista y confirmación del operador antes de guardar. `gemma4:31b` es un candidato cloud; comparar latencia y exactitud antes de elegir. Gemma 3 oficial tiene 27B, no “Gemma 3 31B”.

## Criterio de modelado · 2026-10-03 · Eventos literales

**Decisión:** registrar por separado cada aviso explícito de persona o vehículo. La entrada de Sushito no contiene datos de automóvil y la salida de la Cadillac no contiene otro movimiento. No añadir hechos que el operador no comunicó.

## Criterio de trabajo · 2026-10-03 · Datos sensibles

Nombres, placas y fotos se mantienen en `data/private/`, ignorado por Git. Si después se usa un remoto GitHub, revisar el contenido antes de subirlo. Los repositorios open source son referencias o posibles dependencias, no un permiso para publicar el padrón.

## Por resolver antes de despliegue

- Equipo anfitrión definitivo y si habrá varios operadores simultáneos.
- Horarios exactos de avisos sin hora; no asumirlos en el corte inicial.
- Confirmación de placas discrepantes Honda casa 12 y BMW casa 6.
- Datos de automóvil del aviso de Sushito: no comunicados; dejar campos vacíos.
