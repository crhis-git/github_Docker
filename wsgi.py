from app import create_app

# Punto de entrada para servidores WSGI como Gunicorn en producción
app = create_app()
