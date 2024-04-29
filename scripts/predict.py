import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib

def load_model(model_path):
    """Cargar el modelo entrenado."""
    model = joblib.load(model_path)
    return model

def preprocess_data(data, preprocessor):
    """Preprocesar los datos de predicción."""
    # Aplicar preprocesamiento a las características
    preprocessed_data = preprocessor.transform(data)
    return preprocessed_data

def predict(model, data, preprocessor):
    """Realizar predicciones con el modelo."""
    # Preprocesar los datos de predicción
    preprocessed_data = preprocess_data(data, preprocessor)
    
    # Realizar predicciones
    predictions = model.predict(preprocessed_data)
    
    return predictions

def main(data_path, model_path):
    """Función principal para cargar el modelo, realizar predicciones y guardar los resultados."""
    # Cargar el modelo entrenado
    trained_model = load_model(model_path)
    
    # Cargar los datos de predicción
    data = pd.read_csv(data_path)
    
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

    # Ajustar el ColumnTransformer a los datos de predicción
    preprocessor.fit(data)
    
    # Realizar predicciones
    predictions = predict(trained_model, data, preprocessor)
    
    # Guardar las predicciones en un archivo CSV.
    predictions_df = pd.DataFrame({'Prediction': predictions})
    predictions_df.to_csv("predictions.csv", index=False)
    print("Predicciones guardadas en predictions.csv")

if __name__ == "__main__":
    data_path = "data/test.csv"       # Ruta al archivo CSV de datos para hacer predicciones
    model_path = "models/model.pkl"       # Ruta para cargar el modelo entrenado
    main(data_path, model_path)
