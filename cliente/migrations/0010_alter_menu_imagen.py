# Generated by Django 4.2.1 on 2023-05-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_menu_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='imagen',
            field=models.ImageField(default='', null=True, upload_to='photos/cover'),
        ),
    ]
