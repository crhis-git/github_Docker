from app import create_app

# Crea la instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    # Servidor de desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)
