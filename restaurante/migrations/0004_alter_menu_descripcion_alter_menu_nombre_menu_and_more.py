# Generated by Django 4.2.1 on 2023-06-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0003_menu_disponibilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='descripcion',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='menu',
            name='nombre_menu',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(default='', max_length=100),
        ),
    ]
