# Generador de datos de prueba, separado de las rutas
def get_demo_data():
    return [
        {
            "id": i, 
            "hostname": f"srv-az-prod-{i:03d}", 
            "rol": "API Gateway" if i % 3 == 0 else "Microservice", 
            "estado": "Running"
        } 
        for i in range(1, 101)
    ]
