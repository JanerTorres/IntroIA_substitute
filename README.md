# PROYECTO SUSTITUTO - Introducción a la Inteligencia Artificial
Created by: Jhon Janer Torres Restrepo
### Competición de Kaggle utilizada: 
https://www.kaggle.com/competitions/ubaar-competition/overview

# Fase 1
## Como usar el proyecto

1. Cargar el archivo kaggle.json con tus credenciales del token generado en tu cuenta de kaggle.
2. Asegurarse de estar incrito en la competición de kaggle.
3. Ejecuta el notebook  [01 - generate data and model](https://github.com/JanerTorres/IntroIA_substitute/blob/master/01%20-%20generate%20data%20and%20model.ipynb) para generar los datos de entrenamiento y de prueba.
4. Sigue el flujo en el notebook para entrenar los modelos y ver cómo se recuperan y evaluan las métricas.

# Fase 2
Sobre el directorio del proyecto abre una terminal y ejecuta
Creamos la imagen de docker
- docker build -t sustituto .
Corremos los scripts para obtener los datos directamente de la competición de kaggle
IMPORTANTE (debes tener detor del proyecto tu archivo kaggle.json del Api de autenticación)
- python download_data.py

Ejecutamos el script train para tener un modelo base en el directorio
- python train.py

Corremos el contenedor
- docker run -it -p 8888:8080 -v ${PWD}:/app sustituto

Verificamos el id del contenedor y copiamos las predicciones a nuestro proyecto local para poder verificar. 
- docker cp <id_contenedor>:/app/predictions.csv .

Finalmente podemos ver las predicciones generadas dentro del directorio local
- cat predictions.csv
