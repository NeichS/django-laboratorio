# Generated by Django 5.0.3 on 2024-05-17 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('route', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departure_arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_arrival', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arrival_routes', to='route.route')),
                ('fk_departure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departure_routes', to='route.route')),
            ],
        ),
    ]
