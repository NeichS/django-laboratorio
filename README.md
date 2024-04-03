# django-laboratorio


Paso 1 instalar dependencias:

pip install requirements.txt

pip install psycopg|| pip install psycopg-binary (probar con el primer comando y si $python manage.py makemigrations no funciona, instalar la segunda opcion)

Paso 2 configurar variables de entorno :

copiar '.env.template' y renombrarlo a '.env' tanto en django-project/ como en django-project/project/

Asegurarse de que 'django-project/.env' y 'django-project/project/.env' sean iguales ❗❗


Paso 3 levantar contenedor 🐋: 
docker compose up -d 