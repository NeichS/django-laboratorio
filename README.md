
# Git clone guide

## Recomendacion (opcional)

- Es recomendable tener las dependencias del proyecto en un entorno virtual:

    ```bash
    pip3 install virtualenv #Instala las variables de entorno
    virtualenv venv # crea la carpeta Venv 
    ```

## Paso 1 instalar dependencias

- El archivo requirements.txt posee todas las dependencias del proyecto
    ```bash
    pip install -r requirements.txt #instala dependencias del proyecto

    pip install psycopg
    ```
    
    

***obs***: probar con el primer comando y si python manage.py makemigrations no funciona, instalar la segunda opcion

- Segunda opcion
    ```bash
    pip install psycopg-binary 
    ```
    

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





