# Repositorios candidatos y documentación oficial consultada

| Componente | Repo | Uso | Licencia / nota |
|---|---|---|---|
| PocketBase | https://github.com/pocketbase/pocketbase | Backend SQLite, API, auth, realtime | MIT; versión fijada al implementar. https://pocketbase.io/docs/ |
| PocketBase JS SDK | https://github.com/pocketbase/js-sdk | Cliente frontend | MIT |
| Vue core | https://github.com/vuejs/core | Interfaz | MIT |
| Vite | https://github.com/vitejs/vite | Desarrollo y build | MIT |
| Ollama | https://github.com/ollama/ollama | Inferencia opcional | Ver licencia exacta de la versión usada; modelos tienen términos propios. https://docs.ollama.com/ |

Documentación PocketBase para migraciones: https://pocketbase.io/docs/js-migrations/ ; reglas API: https://pocketbase.io/docs/api-rules-and-filters/ ; rutas personalizadas: https://pocketbase.io/docs/js-routing/ ; HTTP de JSVM: https://pocketbase.io/docs/js-sending-http-requests/ .

Ollama Cloud: https://docs.ollama.com/cloud ; salidas estructuradas: https://docs.ollama.com/capabilities/structured-outputs . La API de Ollama Cloud usa nombres de modelo del catálogo actual; no codificar `gemma3:31b` porque Gemma 3 oficial ofrece 27B. Para cloud se evaluará `gemma4:31b` y se confirmará disponibilidad antes de instalar.

La elección de estos componentes no está cerrada. No se ha clonado una app ajena ni se han publicado datos privados. Si se usan, mantener lockfile, licencia y atribución.
