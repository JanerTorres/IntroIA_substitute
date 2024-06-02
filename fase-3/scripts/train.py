import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib

def load_data(data_path):
    """Cargar los datos de entrenamiento."""
    data = pd.read_csv(data_path)
    return data

def preprocess_data(data):
    """Preprocesar los datos."""
    # Definir columnas numéricas y categóricas
    numeric_features = ['sourceLatitude', 'sourceLongitude', 'destinationLatitude', 'destinationLongitude', 'distanceKM', 'taxiDurationMin', 'weight']
    categorical_features = ['SourceState', 'destinationState', 'vehicleType', 'vehicleOption']

    # Definir transformadores para las columnas numéricas y categóricas
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),  # Imputa los valores faltantes con la mediana
        ('scaler', StandardScaler())  # Escala las características numéricas
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),  # Imputa los valores faltantes con la moda
        ('encoder', OneHotEncoder(handle_unknown='ignore'))  # Codifica las variables categóricas con One-Hot Encoding
    ])

    # Combinar los transformadores en un ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features),
        ]
    )

    # Aplicar preprocesamiento a las características
    preprocessed_data = preprocessor.fit_transform(data)
    
    return preprocessed_data

def train_model(X, y):
    """Entrenar el modelo."""
    # Definir el modelo RandomForestRegressor con los parámetros adecuados
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Entrenar el modelo
    model.fit(X, y)
    
    return model

def main(data_path, model_path):
    """Función principal para cargar los datos, entrenar el modelo y guardar el modelo."""
    # Cargar los datos
    data = load_data(data_path)
    
    # Preprocesar los datos
    X = preprocess_data(data)
    y = data['price']  # Obtiene el objetivo
    
    # Entrenar el modelo
    trained_model = train_model(X, y)
    
    # Guardar el modelo entrenado
    joblib.dump(trained_model, model_path)
    print("Modelo guardado en", model_path)

if __name__ == "__main__":
    data_path = "data/train.csv"              # Ruta al archivo CSV de entrenamiento
    model_path = "models/model.pkl"    # Ruta para guardar el modelo entrenado
    main(data_path, model_path)
