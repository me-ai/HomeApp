# Generated by Django 3.2.7 on 2021-09-25 15:11

import Api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_on', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Thermostat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('tempature', models.CharField(max_length=4, validators=[Api.models.validate_temp])),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
