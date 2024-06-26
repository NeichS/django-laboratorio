# Generated by Django 5.0.3 on 2024-05-17 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_code', models.CharField(max_length=100, unique=True)),
                ('fk_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.city')),
            ],
        ),
    ]
