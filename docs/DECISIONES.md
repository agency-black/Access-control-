# Decisiones y cuestiones abiertas

## ADR 001 · 2026-10-03 · Una base de eventos

**Decisión:** PocketBase/SQLite será la fuente operativa. Excel se exporta para consulta y respaldo manual, no se edita en paralelo. Motivo: un evento inmutable y el estado derivado evitan versiones DOCX/XLSX divergentes. La instancia inicial es local; si hay varios dispositivos, una instancia en la red local.

## ADR 002 · 2026-10-03 · Modelo como intérprete

**Decisión:** Ollama Cloud opcional con salida JSON estructurada; validación determinista y confirmación del operador antes de guardar. `gemma4:31b` es candidato de inicio para cloud; comparar latencia y exactitud con frases reales antes de fijarlo. Gemma 3 oficial tiene 27B, no “Gemma 3 31B”. La falta de clave no bloquea el trabajo manual.

## ADR 003 · 2026-10-03 · Persona y vehículo separados

**Decisión:** un vehículo visitante puede salir sin confirmar salida de su conductor. Sushito puede entrar sin automóvil. No inferir ubicación de residentes a partir de todos los autos de la casa. Esta separación corrige el límite del prototipo Python inicial.

## ADR 004 · 2026-10-03 · Datos sensibles

**Decisión:** nombres, placas, fotos y base se mantienen en `data/private/` y `pb_data/`, ambos ignorados por Git. El proyecto puede convertirse en repositorio GitHub **privado** después de revisar el primer commit. Nunca publicar datos privados en un repo open source. Usar proyectos open source como dependencias, no hacer público el padrón.

## Por resolver antes de despliegue

- Equipo anfitrión definitivo y si habrá varios operadores simultáneos.
- Horarios exactos de avisos sin hora; no asumirlos en el corte inicial.
- Confirmación de placas discrepantes Honda casa 12 y BMW casa 6.
- ¿Hugo se fue en la Cadillac? Actualmente desconocido.
- Nombre legal de “Sushito” y si llegó a pie o en otro vehículo: no comunicado.
