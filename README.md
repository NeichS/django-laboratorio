# django-laboratorio


Paso 1 instalar dependencias:

pip install -r requirements.txt

pip install psycopg|| pip install psycopg-binary (probar con el primer comando y si $python manage.py makemigrations no funciona, instalar la segunda opcion)

Paso 2 configurar variables de entorno :

copiar '.env.sample' y renombrarlo a '.env' 

Paso 3 levantar contenedor 🐋: 
docker compose up -d 

