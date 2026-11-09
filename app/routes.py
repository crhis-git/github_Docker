from flask import Blueprint, render_template
from app.demo_data import get_demo_data

# Se define un Blueprint para organizar las rutas
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/data')
def data_list():
    # Llamamos a la lógica separada
    data = get_demo_data()
    return render_template('data.html', data=data)

@main.route('/about')
def about():
    content = "<h1>Acerca de</h1><p>Esta es una app Flask modular orientada a producción y CI/CD.</p>"
    return render_template('base.html', title="Acerca de", content=content)
