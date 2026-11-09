from flask import Flask

def create_app():
    # Application Factory Pattern
    app = Flask(__name__)
    
    # Registrar los Blueprints (Rutas)
    from app.routes import main
    app.register_blueprint(main)
    
    return app
