# Memoria exclusiva: app de portería

**Corte de contexto:** 3 de octubre de 2026, aviso más reciente 15:06 en Ciudad de México. La memoria pertenece solo a la construcción de la app. El Excel y las tablas existentes de la conversación continúan en uso; cualquier movimiento posterior allí prevalece sobre este corte. No se acordó migrar la operación a la app todavía.

## Problema y preferencia del operador

El operador recibe autos y visitas en una portería. Debe buscar de inmediato si un automóvil/persona está en el padrón, con **sí/no, nombre, placa y casa**; distinguir visitas; registrar salidas y entradas; y saber quiénes siguen sin regreso anotado. La app se construye como proyecto separado para agilizar ese trabajo. **Las tablas y el Excel que ya se usan aquí siguen vigentes durante la construcción.** Las respuestas de operación deben ser cortas y precisas.

## Fuentes privadas exportadas

- `data/private/raw/registro_consulta_actual.json`: padrón revisado 6 (17 casas, 43 vehículos residentes, 4 vehículos de visitas conocidas). Contiene nombres, placas, colores, tipos, notas y referencias de imagen.
- `data/private/raw/bitacora_data.json`: 31 eventos, dos visitas nombradas y los avisos del operador hasta 15:06.
- `data/private/raw/avisos_usuario_literales.json`: frases exactas de los avisos recientes. Para Hugo/Cadillac/Sushito, estas frases prevalecen sobre anotaciones añadidas previamente al JSON intermedio.
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
- Hugo Hernández entró como visita a casa 12 con Cadillac negra **15:02**. **Salió la Cadillac 15:04**. Son los dos avisos recibidos; no agregar otra salida de persona.
- Sushito entró como visita a casa 12 **15:06**. Ese aviso no aporta datos de vehículo; el evento queda asociado a la persona y `vehicle_id = null`.

## Dudas del padrón que no deben “corregirse” por intuición

- Honda casa 12: en la foto la placa parece `076850`, padrón `076840`; la entrada está marcada “E” sin hora.
- BMW casa 6 `5SK 172`: placa manuscrita poco clara; se vinculó por casa/auto, confirmar físicamente.
- “Lucía” figura conduciendo el Fiat `725 YNN` de casa 10, pero no consta como residente de esa casa; no atribuirle identidad residencial automáticamente.
- Varias marcas/modelos están incompletos, como Geli casa 17, Honda casa 3 y Mercedes casa 3. Las miniaturas de internet son referencias de modelo/color, no fotos probatorias del vehículo real.

## Decisión técnica vigente

**Propuesta técnica por evaluar, no decisión del usuario:** PocketBase + Vue 3/Vite, con Ollama opcional para interpretar frases. Se investigaron repositorios abiertos de GitHub. El objetivo del proyecto es construir y probar la app; no cambiar aún el flujo de tablas actual.

## Próximo trabajo concreto

Evaluar el stack con el usuario y construir un prototipo sobre **copias** del corte de contexto; después implementar búsqueda, captura y visitas. Probar sin tocar el Excel ni el padrón actuales. Cualquier migración o sincronización se decide más adelante de forma explícita.
