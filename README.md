# App de portería

Proyecto aislado **de construcción de una app** para casas, vehículos, personas y visitas. El corte privado del 3 de octubre de 2026 está en `data/private/`. Este repositorio contiene contexto, datos copiados, reglas de trabajo, opciones técnicas y tareas. **Las tablas y el Excel actuales de la conversación siguen en uso y se siguen actualizando.** Este proyecto no los sustituye ni les cambia datos.

## Punto de partida

1. Leer `AGENTS.md` y `MEMORIA_PROYECTO.md`.
2. Verificar el corte privado: `python3 tools/export_snapshot.py`.
3. Leer `docs/REQUISITOS.md`, `docs/MODELO_DATOS.md`, `docs/ARQUITECTURA.md` y `docs/PLAN.md`.
4. Construir y probar sobre una copia de los datos, sin modificar las tablas actuales.

El corte incluye 17 casas, 43 vehículos residentes, 4 vehículos de visitas previamente conocidos, una Cadillac de visita y 31 eventos. La entrada de Sushito se registra con los datos comunicados, sin agregar un automóvil. El estado de 26 vehículos residentes no tiene movimiento anotado.

## Repositorios abiertos elegidos

- [PocketBase](https://github.com/pocketbase/pocketbase): servidor con SQLite, autenticación, API y tiempo real. Licencia MIT.
- [PocketBase JS SDK](https://github.com/pocketbase/js-sdk): cliente oficial. Licencia MIT.
- [Vue core](https://github.com/vuejs/core): interfaz. Licencia MIT.
- [Vite](https://github.com/vitejs/vite): compilación y desarrollo. Licencia MIT.
- [Ollama](https://github.com/ollama/ollama): cliente/servidor de modelos. El modelo cloud se configura por clave en el servidor y es opcional.

No se han clonado ni modificado esos repositorios en esta carpeta. La aplicación propia usará sus paquetes o binarios y mantendrá la atribución/licencia correspondiente. El código privado y las placas no se publican automáticamente en GitHub.

## Archivos privados y control de versiones

`data/private/` contiene nombres, placas y fotos. `.gitignore` impide que entren en un commit normal. El archivo comprimido de entrega del proyecto **sí contiene** esta carpeta para conservar el corte. Si se crea más adelante un repositorio remoto, será necesario decidir expresamente si será privado y comprobar `git status` antes de subirlo.

El Excel incluido en `data/private/reference/` es una **copia fechada para contexto**. El Excel actual fuera de este proyecto continúa siendo el instrumento de trabajo. No se ha decidido migrarlo ni sincronizarlo con la app.
