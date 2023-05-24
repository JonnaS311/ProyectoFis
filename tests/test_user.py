import pytest 
import datetime

from cliente.models import *

@pytest.mark.django_db
def test_creacion_pedido():
    pedido = Pedido.objects.create(
        fecha = datetime.date(1999,10,22),
        estado = 'listo'
    )
    assert pedido.fecha == datetime.date(1999,10,22)
    assert pedido.estado == 'listo'
 
    
@pytest.mark.django_db
def test_creacion_pedido_error():
    with pytest.raises(Exception):
        Pedido.objects.create(
            fecha = datetime.date(2999,19,21),
            estado = 'rojas'
        )

@pytest.mark.django_db
def test_creacion_cliente():
    cliente = Client.objects.create(
        name = 'loco',
        password = "12345",
        telefono = 3133526413,
        direccion_cliente = 'carrera 62 # 9 - 18'
    )
    assert cliente.name == 'loco'
    assert cliente.password == "12345"
    assert cliente.telefono == 3133526413
    assert cliente.direccion_cliente == 'carrera 62 # 9 - 18'