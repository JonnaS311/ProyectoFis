# Generated by Django 4.2.1 on 2023-05-07 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_fijo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_variable', models.IntegerField()),
                ('nombre_menu', models.CharField(default='', max_length=50)),
                ('descripcion', models.CharField(default='', max_length=200)),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.ingrediente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_fijo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.PositiveIntegerField()),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.ingrediente')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.menu')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_sede', models.CharField(max_length=30)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(max_length=30)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.sede')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.producto'),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('telefono', models.PositiveIntegerField()),
                ('direccion_cliente', models.CharField(max_length=30)),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.pedido')),
            ],
        ),
    ]
