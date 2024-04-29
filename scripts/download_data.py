import os
import zipfile
import kaggle

# Configuramos la ruta del archivo kaggle.json
os.environ['KAGGLE_CONFIG_DIR'] = "data"

# Descargar los archivos de la competición directamente desde Kaggle
kaggle.api.competition_download_files("ubaar-competition", path="data")

# Descomprimir el archivo descargado
zip_file = "data/ubaar-competition.zip"
extract_dir = "data"
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# Eliminar el archivo zip después de la extracción si lo deseas
os.remove(zip_file)
