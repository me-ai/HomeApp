# Generated by Django 3.2.7 on 2021-09-25 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_auto_20210925_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logaction',
            old_name='is_on',
            new_name='isOn',
        ),
    ]
