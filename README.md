# PROYECTO SUSTITUTO - Introducción a la Inteligencia Artificial
**Creado por:** Jhon Janer Torres Restrepo

**Competición de Kaggle utilizada:** [Kaggle Competición](https://www.kaggle.com/competitions/ubaar-competition/overview)

## Fase 1: Generación de datos y modelo

### Prerrequisitos:
- Tener instalado **Jupyter Notebook**
- Tener un archivo `kaggle.json` con tus credenciales de Kaggle (ver fase 2)

### Pasos:

1. **Cargar el archivo `kaggle.json`**:
   - Coloca el archivo `kaggle.json` en el directorio raíz del proyecto.

2. **Ejecutar el notebook**:
   - Ejecuta el notebook [01 - generate data and model](https://github.com/JanerTorres/IntroIA_substitute/blob/master/01%20-%20generate%20data%20and%20model.ipynb).
   - Este notebook generará los datos de entrenamiento y prueba, entrenará un modelo y evaluará su rendimiento.

## Fase 2: Despliegue en Docker

### Prerrequisitos:
- Docker instalado
- Archivo `kaggle.json` con tus credenciales de Kaggle (ver instrucciones a continuación)

### Pasos:

1. **Obtener el archivo `kaggle.json`**:
   - Inicia sesión en tu cuenta de Kaggle.
   - Ve a la sección de tu perfil y selecciona "API".
   - Genera un nuevo token de API y descarga el archivo `kaggle.json`.
   - Coloca el archivo `kaggle.json` en el directorio `fase-2` del proyecto.

2. **Construir la imagen Docker**:
   - Navega al directorio `fase-2`: `cd fase-2`
   - Ejecuta el comando: `docker build -t fase-2 .`

3. **Ejecutar el contenedor Docker**:
   - Ejecuta el comando: `docker run -it -p 8888:8080 -v ${PWD}:/app fase-2` Esto ejecutará el contenedor, montando el directorio actual (`$PWD`) en `/app` dentro del contenedor.

   - (Si sale un mensaje de que el achivo `test.csv` NO EXISTE, recomiendo ejecutar el archivo `download_data.py` en el ambiente local para que se descargue la carpeta `data` y luego copiar esta carpeta al directorio `fase-2` para que cuando el contenedor intente guardar el archivo de predicciones, encuentre una ruta en local, ya que este directorio de `/data` solo estaría disponible dentro del contenedor)

   ### En caso que no se genere el archivo `predictions.csv` dento del directorio `fase-2` hacer lo siguiente:
   - Verificamos el id del contenedor co el comando `docker ps -a` 8fa8de7f895e
   - Ejecutar el comando `docker cp <id_container>:/app/predictions.csv data/`para copiar el archivo generado a nuestro ambiente local en la ruta /fase-2/data/ y poder verificar su existencia en el docker lanzado.

4. **Verificar el contenedor**:
   - Puedes verificar si el contenedor está en ejecución utilizando el comando: `docker ps`

5. **Generar predicciones**:
   - Dentro del contenedor, ejecuta el script: `python predict.py`
   - Esto generará las predicciones y las guardará en el archivo `predictions.csv` dentro del contenedor.

6. **Copiar las predicciones**:
   - Para copiar las predicciones al directorio local, ejecuta el comando: `docker cp <id_contenedor>:/app/predictions.csv .`
   - Reemplaza `<id_contenedor>` con el ID del contenedor que obtuviste en el paso 4.

7. **Visualizar las predicciones**:
   - Puedes ver las predicciones generadas abriendo el archivo `predictions.csv` en tu editor de texto favorito.

### Notas adicionales:
- Asegúrate de que todos los archivos necesarios (como `test.csv` y `model.pkl`) estén en las ubicaciones correctas dentro del proyecto antes de construir la imagen Docker.
- Si necesitas actualizar las dependencias, asegúrate de modificar el archivo `requirements.txt` y reconstruir la imagen Docker.


## Fase 3: Despliegue en Docker
#### Pasos para Ejecutar

1.  **Construir la Imagen Docker**
    
    Abre una terminal en el directorio que contiene el archivo `Dockerfile` de la Fase-3 y ejecuta el siguiente comando para construir la imagen Docker:
    
    ```bash
    docker build -t fase-3 .
    ```
    
2.  **Ejecutar el Contenedor Docker**
    
    Después de construir la imagen Docker, ejecuta el siguiente comando para crear y ejecutar un contenedor Docker:
    
    ```bash
    docker run -d -p 5001:5001 fase-3
    ```
    
    Este comando creará y ejecutará un contenedor Docker basado en la imagen `fase-3`. El parámetro `-d` indica que el contenedor se ejecutará en segundo plano, y `-p 5001:5001` mapea el puerto 5001 del contenedor al puerto 5001 del host, permitiendo acceder a la aplicación Flask desde tu máquina local.
    
3.  **Verificar la Ejecución del Contenedor**
    
    Para asegurarte de que el contenedor está en ejecución, ejecuta el siguiente comando:
    
    ```bash
    docker ps
    ```
    
    Este comando mostrará una lista de todos los contenedores en ejecución en tu sistema. Verifica que el contenedor de la fase-3 esté en la lista.
    
4.  **Acceder a la Aplicación**
    
    Una vez que el contenedor esté en ejecución, puedes acceder a la aplicación Flask desde tu navegador web o mediante herramientas como `curl` o `Postman`. La URL de acceso será `http://localhost:5001`.
    

#### Notas Importantes

*   Asegúrate de tener los puertos necesarios (en este caso, el puerto 5001) disponibles en tu sistema para evitar conflictos.
*   Si encuentras algún problema durante la construcción o ejecución del contenedor, verifica los mensajes de error y busca soluciones en línea o consulta a un desarrollador para obtener ayuda.

Con estos pasos, deberías poder ejecutar la Fase-3 de nuestro proyecto sin problemas. ¡Disfruta explorando la aplicación!

