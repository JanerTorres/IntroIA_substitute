import os
import zipfile
import kaggle

# Configuramos la ruta del archivo kaggle.json
os.environ['KAGGLE_CONFIG_DIR'] = "/root/.kaggle"

# Creamos el directorio data si no existe
if not os.path.exists('data'):
    os.makedirs('data')

# Descargar los archivos de la competición directamente desde Kaggle
print("Descargando archivos de la competición...")
kaggle.api.competition_download_files("ubaar-competition", path="data")
print("Descarga completa.")

# Descomprimir el archivo descargado
zip_file = "data/ubaar-competition.zip"
extract_dir = "data"
print(f"Descomprimiendo {zip_file} en {extract_dir}...")
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)
print("Descompresión completa.")

# Verificar si el archivo test.csv existe
test_csv = os.path.join(extract_dir, 'test.csv')
if os.path.exists(test_csv):
    print(f"El archivo {test_csv} ha sido encontrado.")
else:
    print(f"El archivo {test_csv} NO ha sido encontrado.")

# Eliminar el archivo zip después de la extracción si lo deseas
os.remove(zip_file)
