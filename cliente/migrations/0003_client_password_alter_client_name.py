# Generated by Django 4.2.1 on 2023-05-14 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
