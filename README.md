# Docker CI/CD Azure App Demo

Esta es una aplicación Flask con arquitectura modular, lista para despliegues en producción usando Docker y Gunicorn.

## Estructura
- `app/`: Contiene la lógica principal de la aplicación.
- `run.py`: Para ejecutar el servidor de desarrollo local.
- `wsgi.py`: Punto de entrada para el servidor de producción (Gunicorn).
