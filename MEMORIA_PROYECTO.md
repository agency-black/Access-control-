# Memoria exclusiva: app de portería

**Corte semilla:** 3 de octubre de 2026, aviso más reciente 15:06 en Ciudad de México. La memoria de este archivo pertenece a este proyecto. Los movimientos posteriores vivirán en la base operativa y prevalecerán sobre este corte.

## Problema y preferencia del operador

El operador recibe autos y visitas en una portería. Debe buscar de inmediato si un automóvil/persona está en el padrón, con **sí/no, nombre, placa y casa**; distinguir visitas; registrar salidas y entradas; y saber quiénes siguen sin regreso anotado. El flujo anterior creó múltiples DOCX y XLSX divergentes, omitió el número de casa en una vista y confundió falta de registro con presencia. El operador quiere **una app ágil y una base única**, sin generar otro documento por cada aviso. Las respuestas en turno deben ser cortas y precisas.

## Fuentes privadas exportadas

- `data/private/raw/registro_consulta_actual.json`: padrón revisado 6 (17 casas, 43 vehículos residentes, 4 vehículos de visitas conocidas). Contiene nombres, placas, colores, tipos, notas y referencias de imagen.
- `data/private/raw/bitacora_data.json`: 31 eventos, dos visitas nombradas y los avisos del operador hasta 15:06.
- `data/private/raw/bitacora_fotos/`: cuatro fotografías de la bitácora manuscrita original.
- `data/private/reference/bitacora_2026-10-03_1506.xlsx`: copia del Excel operativo al corte, para contraste. No editarlo como base viva.
- `data/private/export/`: entidades normalizadas e `manifest.json` con conteos, limitaciones y hashes SHA-256. Se regeneran con `python3 tools/export_snapshot.py` desde las dos fuentes JSON copiadas **solo para validar el corte**, nunca para sobrescribir una base con eventos posteriores.

## Estado al corte, solo vehículos de residentes

| Última salida sin entrada posterior | Casa | Placas | Hora |
|---|---:|---|---|
| Renault Duster | 1 | AI4 AMX | 14:31 |
| Honda (Pilot en foto, modelo pendiente en padrón) | 3 | N35 BSK | 08:00 |
| Hyundai Tucson | 6 | MZG 684A | 14:00 |
| GWM Haval | 7 | 68G675 | 13:36 |
| BYD | 14 | 72G 347 | 06:11 |
| Geli (marca por confirmar) | 17 | 33H423 | 12:05 |

**Conteos:** 6 con última salida, 11 con última entrada, 26 sin movimiento observado, total 43. “Última entrada” y “última salida” describen vehículos, no garantizan la ubicación de todos los residentes.

## Avisos recientes críticos

- Mustang Mach-E negro, casa 12, placa `60G043`: salió 12:02; entró **14:32**. En la foto figura conductor “Ramiro”; el padrón de casa 12 dice Cynthia de la Borboya y Demian Gtz. No igualar Ramiro con Demian.
- Renault Duster gris, casa 1, `AI4 AMX`: salió **14:31**, conductor no comunicado.
- Jetta gris, casa 2, `D86 BAH`: entrada avisada alrededor de las 14:50, **hora de llegada no indicada**. Guardar `time = null`, `reported_at` aparte si disponible.
- Hugo Hernández entró como visita a casa 12 en Cadillac negra **15:02**, sin placas. **La Cadillac salió 15:04**; no se confirmó si Hugo iba a bordo. Estado del vehículo = última salida; presencia de Hugo = desconocida.
- Sushito entró como visita a casa 12 **15:06**. No se comunicaron automóvil, placas, color ni nombre legal. Es evento de persona con `vehicle_id = null`.

## Dudas del padrón que no deben “corregirse” por intuición

- Honda casa 12: en la foto la placa parece `076850`, padrón `076840`; la entrada está marcada “E” sin hora.
- BMW casa 6 `5SK 172`: placa manuscrita poco clara; se vinculó por casa/auto, confirmar físicamente.
- “Lucía” figura conduciendo el Fiat `725 YNN` de casa 10, pero no consta como residente de esa casa; no atribuirle identidad residencial automáticamente.
- Varias marcas/modelos están incompletos, como Geli casa 17, Honda casa 3 y Mercedes casa 3. Las miniaturas de internet son referencias de modelo/color, no fotos probatorias del vehículo real.

## Decisión técnica vigente

PocketBase (SQLite, API, autenticación y tiempo real) + Vue 3/Vite para interfaz, con importador del corte y lógica de eventos. Ollama Cloud mediante ruta de servidor para interpretar frases en JSON; la captura manual funciona sin IA. Versionar dependencias y migraciones. Esta decisión puede revisarse con evidencia, pero no regresar a documentos como sistema operativo.

## Próximo trabajo concreto

Implementar colecciones/migración, importación idempotente de `data/private/export/`, consulta y captura con transacción; luego interfaz de búsqueda/pendientes/visitas; finalmente interpretación Ollama y exportación XLSX bajo demanda. Validar primero los ejemplos de `AGENTS.md`.
