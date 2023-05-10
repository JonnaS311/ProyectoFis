# Generated by Django 4.2.1 on 2023-05-10 12:42

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
                ('nombre_ingrediente', models.CharField(default='', max_length=50)),
                ('precio_fijo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_variable', models.IntegerField()),
                ('nombre_menu', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(default='', null=True, upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(default='', max_length=50)),
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
        migrations.CreateModel(
            name='MenuProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.menu')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.producto')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='producto',
            field=models.ManyToManyField(blank=True, through='cliente.MenuProducto', to='cliente.producto'),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('telefono', models.PositiveIntegerField()),
                ('direccion_cliente', models.CharField(max_length=30)),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.pedido')),
            ],
        ),
    ]
