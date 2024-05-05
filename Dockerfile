FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
# Python no generará archivos de byte compilado (.pyc)
ENV PYTHONUNBUFFERED 1 
# PYTHONNUMBUFFERED 1-> la salida de los comandos de Python se enviará directamente a la consola sin almacenarla en un búfer intermedio,

# Set the working directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY ./django-project .
EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

# CMD ["tail", "-f", "/dev/null"]
