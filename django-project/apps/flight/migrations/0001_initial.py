# Generated by Django 5.0.3 on 2024-05-03 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('stopover', models.BooleanField()),
                ('departure_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FlightHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plane_model', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('chico', 'chico'), ('mediano', 'mediano'), ('grande', 'grande')], default='mediano', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_date', models.DateField()),
                ('ticket_class', models.CharField(max_length=50)),
                ('pourchase_date', models.DateField()),
                ('seat_location', models.CharField(max_length=50)),
            ],
        ),
    ]