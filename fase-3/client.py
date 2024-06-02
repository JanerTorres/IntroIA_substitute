import requests

# Endpoint para realizar predicciones
predict_endpoint = 'http://0.0.0.0:5000/predict'

# Datos de entrada para la predicción
data = {
    "sourceLatitude": 37.7749,
    "sourceLongitude": -122.4194,
    "destinationLatitude": 34.0522,
    "destinationLongitude": -118.2437,
    "distanceKM": 600,
    "taxiDurationMin": 180,
    "weight": 10,
    "SourceState": "California",
    "destinationState": "New York",
    "vehicleType": "Car",
    "vehicleOption": "Option 1"
}

# Realizar la solicitud POST para obtener la predicción
response = requests.post(predict_endpoint, json=data)

# Imprimir la respuesta
print("Predicción:", response.json())

# Endpoint para entrenar el modelo
train_endpoint = 'http://0.0.0.0:5000/train'

# Realizar la solicitud GET para entrenar el modelo
train_response = requests.get(train_endpoint)

# Imprimir la respuesta del entrenamiento
print("Entrenamiento:", train_response.text)
