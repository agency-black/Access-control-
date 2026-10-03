# Requisitos de operación

## Usuario y flujo

Operador de portería en México, horario `America/Mexico_City`. El panel principal abre con búsqueda grande, seis vehículos con última salida, visitas con última entrada y un botón para registrar entrada/salida. La consulta por “Mustang negro” debe mostrar casa 12, placa 60G043, padrón y último movimiento. Al informar “ya llegó el Jetta”, debe seleccionar la coincidencia y guardar entrada sin inventar hora; la hora de aviso puede quedar en otro campo.

## Vistas

1. **Consulta rápida**: placa, marca/modelo, color, nombre y casa. Resultado exacto o lista de coincidencias; si la búsqueda es ambigua, no responder sí/no de manera falsa.
2. **Pendientes**: vehículos con último evento `out` sin `in` posterior, con casa, placa, persona anotada, color y hora. Los autos sin registro figuran aparte como `Sin dato`.
3. **Movimientos**: secuencia inmutable, hora opcional, casa obligatoria, fuente, operador, correcciones vinculadas. Filtros por fecha, casa, placa, persona.
4. **Visitas**: identidad, casa anfitriona, vehículo opcional, entrada/salida de persona por separado del movimiento del automóvil. Sin placa permitida.
5. **Padrón**: vehículos y residentes de referencia; cambios auditados y evidencia/observación previa conservada.
6. **Exportación**: XLSX/CSV manual del estado y bitácora con fecha de corte; no crear documentos nuevos por cada evento.

## Captura rápida

- Botones `Entró` y `Salió`, autocompletar vehículo/persona, casa visible, hora local editable y nota opcional.
- Si solo se menciona un modelo/color y hay varios matches, ofrecer selección. La placa exacta gana cuando es única.
- Duplicado de mismo aviso: usar un `client_event_id` idempotente y advertir si la última acción ya coincide. Permitir rectificación explícita, no borrar la fila anterior.
- Mostrar confirmación concreta: `Casa 12 · Mustang negro · 60G043 · Entró 14:32`.
- El modelo convierte lenguaje natural o una foto en una **propuesta**, nunca ejecuta un alta ni cambia un registro. Guardado final por botón y validaciones deterministas.

## Privacidad y confiabilidad

- Autenticación de operadores; acceso a nombres/placas restringido. No exponer API de escritura anónima ni clave de Ollama al navegador.
- Copia de seguridad de SQLite y prueba de restauración; corte anterior recuperable.
- Funcionar en la red local sin modelo. Si Ollama Cloud falla, la captura manual continúa.
- No prometer margen de error cero: los campos dudosos quedan marcados y requieren confirmación humana. Mantener historial de quién/qué/cuándo/fuente.

## Pruebas de aceptación del primer incremento

- `Mustang negro` → un vehículo, casa 12, 60G043, último `in` 14:32.
- `Renault` → casa 1, AI4 AMX, último `out` 14:31.
- `Jetta` → casa 2, D86 BAH, último `in`, hora de llegada desconocida.
- `Sushito` → visita casa 12, persona entró 15:06, sin vehículo.
- `Cadillac negra` → vehículo de visita salió 15:04; Hugo: presencia desconocida.
- Conteos de residentes 6/11/26; agregar visita no los altera.
