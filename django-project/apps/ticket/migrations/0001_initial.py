# Generated by Django 5.0.3 on 2024-05-17 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flight', '0001_initial'),
        ('itinerary', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_date', models.DateField()),
                ('ticket_class', models.CharField(max_length=50)),
                ('pourchase_date', models.DateField()),
                ('seat_location', models.CharField(max_length=50)),
                ('fk_flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
                ('fk_itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itinerary.itinerary')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]