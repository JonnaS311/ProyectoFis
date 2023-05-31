# Generated by Django 4.2.1 on 2023-05-29 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='disponibilidad',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menu',
            name='restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.restaurante'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.restaurante'),
        ),
    ]
