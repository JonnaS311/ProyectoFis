# Generated by Django 4.2.1 on 2023-05-07 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_alter_menu_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='ingrediente',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='producto',
        ),
    ]
