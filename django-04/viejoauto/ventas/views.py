from django.shortcuts import render
from .models import Venta
from django.db import connection


def listar_ventas(request):
    cursor = connection.cursor()
    sql = [
        'SELECT ',
        'v.observaciones as obs, v.fecha_venta as fecha, ',
        'a.placa, cven.dni dni_v, ccom.dni dni_c, ',
        '(uven.first_name||\' \'||uven.last_name) vendedor, ',
        '(ucom.first_name||\' \'||ucom.last_name) comprador ',
        'FROM ventas_venta v ',
        'JOIN automoviles_automovil a ON a.id=v.automovil_id ',
        'JOIN clientes_cliente cven ON v.vendedor_id=cven.id ',
        'JOIN clientes_cliente ccom ON v.comprador_id=ccom.id ',
        'JOIN auth_user uven ON uven.id=cven.usuario_id ',
        'JOIN auth_user ucom ON ucom.id=ccom.usuario_id ',
        'WHERE v.comprador_id <> v.vendedor_id ',
    ]
    sql = ''.join(sql)
    rows = cursor.execute(sql)

    return render(request, 'ventas/reporte.html', {
        'allobjects': Venta.objects.all(),
        'rows': rows
    })

