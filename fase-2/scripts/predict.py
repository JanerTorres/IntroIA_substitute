import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib
import os

def load_model(model_path):
    """Cargar el modelo entrenado."""
    print(f"Cargando el modelo desde {model_path}")
    model = joblib.load(model_path)
    return model

def preprocess_data(data, preprocessor):
    """Preprocesar los datos de predicción."""
    print("Preprocesando los datos...")
    preprocessed_data = preprocessor.transform(data)
    return preprocessed_data

def predict(model, data, preprocessor):
    """Realizar predicciones con el modelo."""
    preprocessed_data = preprocess_data(data, preprocessor)
    print("Realizando predicciones...")
    predictions = model.predict(preprocessed_data)
    return predictions

def main(data_path, model_path):
    """Función principal para cargar el modelo, realizar predicciones y guardar los resultados."""
    # Verificar si el archivo CSV de datos existe
    if not os.path.exists(data_path):
        print(f"Error: El archivo {data_path} no existe.")
        return

    # Verificar si el modelo existe
    if not os.path.exists(model_path):
        print(f"Error: El archivo del modelo {model_path} no existe.")
        return

    # Cargar el modelo entrenado
    trained_model = load_model(model_path)

    # Cargar los datos de predicción
    print(f"Cargando datos de predicción desde {data_path}")
    data = pd.read_csv(data_path)

    # Definir columnas numéricas y categóricas
    numeric_features = ['sourceLatitude', 'sourceLongitude', 'destinationLatitude', 'destinationLongitude', 'distanceKM', 'taxiDurationMin', 'weight']
    categorical_features = ['SourceState', 'destinationState', 'vehicleType', 'vehicleOption']

    # Definir transformadores para las columnas numéricas y categóricas
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combinar los transformadores en un ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features),
        ]
    )

    # Ajustar el ColumnTransformer a los datos de predicción
    print("Ajustando el ColumnTransformer a los datos de predicción...")
    preprocessor.fit(data)

    # Realizar predicciones
    predictions = predict(trained_model, data, preprocessor)

    # Guardar las predicciones en un archivo CSV en la raíz
    output_path = "predictions.csv"
    predictions_df = pd.DataFrame({'Prediction': predictions})
    predictions_df.to_csv(output_path, index=False)
    print(f"Predicciones guardadas en {output_path}")

if __name__ == "__main__":
    data_path = "/app/data/test.csv"  # Ruta al archivo CSV de datos para hacer predicciones
    model_path = "/app/models/model.pkl"  # Ruta para cargar el modelo entrenado
    main(data_path, model_path)
