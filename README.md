
# Git clone guide

## Recomendación (opcional)

- Es recomendable tener las dependencias del proyecto en un entorno virtual:

    ```bash
    pip3 install virtualenv #Instala las variables de entorno
    virtualenv venv # crea la carpeta Venv 
    ```

## Paso 1 instalar dependencias

- El archivo requirements.txt posee todas las dependencias del proyecto
    ```bash
    pip install -r requirements.txt #instala dependencias del proyecto


## Paso 2 configurar variables de entorno 

- copiar '.env.sample' y renombrarlo a '.env' (no tocar .env.sample) 


## Paso 3 levantar contenedor 🐋

- Te paras en el directorio donde se encuentra docker-compose.yml no seas bot
    ```bash
    docker compose up -d # -d para ejecutar en segundo plano
    ```

## Paso 4 ejecutar django:

- Dirigirse donde se encuentra manage.py 
- ejecutar los siguientes comandos:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver #{puerto a eleccion} por defecto utiliza el puerto 8000
    ```



## Convenciones a seguir

- clases en PascalCase
- metodos en camelCase
- variables en snake_case
- directorios con guion-medio 

***obs***:  si es una aplicacion de django el directorio va a tener que ser con guion_bajo 


## Creacion de aplicaciones


- Una vez parado en el directorio apps/

     ```bash
    python ../manage.py startapp nombre_aplicacion
    ```
***obs***: No es necesario crear la carpeta con el nombre de la aplicacion

