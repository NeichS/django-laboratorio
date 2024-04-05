
# Paso 1 instalar dependencias:

pip install -r requirements.txt

pip install psycopg|| pip install psycopg-binary (probar con el primer comando y si $python manage.py makemigrations no funciona, instalar la segunda opcion)

# Paso 2 configurar variables de entorno :

copiar '.env.sample' y renombrarlo a '.env' (no tocar .env.sample) 


# Paso 3 levantar contenedor 🐋:

docker compose up -d 

# Paso 4 ejecutar django:

Dirigirse donde se encuentra manage.py 
ejecutar los siguientes comandos
python manage.py makemigrations
python manage.py migrate
python manage.py runserver {puerto a eleccion} por defecto utiliza el puerto 8000






