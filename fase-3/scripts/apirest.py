from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

# Cargar el modelo entrenado
model_path = "/app/models/model.pkl"
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    raise FileNotFoundError("Model file not found at specified path.")

# Definir transformadores para las columnas numéricas y categóricas
numeric_features = ['sourceLatitude', 'sourceLongitude', 'destinationLatitude', 'destinationLongitude', 'distanceKM', 'taxiDurationMin', 'weight']
categorical_features = ['SourceState', 'destinationState', 'vehicleType', 'vehicleOption']

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features),
    ]
)

def preprocess_data(data):
    preprocessed_data = preprocessor.transform(data)
    return preprocessed_data

def train_model(X, y):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame(data)
        predictions = model.predict(preprocess_data(df))
        return jsonify({'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/train', methods=['GET'])
def train():
    if request.method == 'GET':
        try:
            data_path = "data/test.csv"
            data = pd.read_csv(data_path)
            X = preprocess_data(data)
            y = data['price']
            trained_model = train_model(X, y)
            return "Modelo entrenado exitosamente"
        except Exception as e:
            return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
