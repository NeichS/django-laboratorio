import os
from dotenv import load_dotenv

load_dotenv()

postgres_db_name = os.getenv("DB_NAME")
postgres_user = os.getenv("DB_USER")
postgres_password = os.getenv("DB_PASSWORD")
postgres_port = os.getenv("DB_PORT")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': postgres_db_name,
        'USER': postgres_user,
        'PASSWORD': postgres_password,
        'HOST': 'localhost',
        'PORT': postgres_port,
    }
}

print(DATABASES['default']['NAME'])
print(DATABASES['default']['USER'])
print(DATABASES['default']['PASSWORD'])
print(DATABASES['default']['PORT'])
