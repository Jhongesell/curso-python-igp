#!/usr/bin/env python

import json
import pprint
from collections import OrderedDict

def cargar_csv(filepath):
    resultado = OrderedDict([
        ('cabeceras', []),
        ('datos', [])
    ])
    registros = [
        linea.strip().split(',') for linea
        in open(filepath).readlines()
        if len(linea.strip()) > 0
    ]
    if len(registros) > 0:
        resultado['cabeceras'] = registros[0]
    if len(registros) > 1:
        resultado['datos'] =  registros[1:]

    return resultado

def registros_con_nombre(cabeceras, registros):
    resultados = []
    for reg in registros:
        aux = OrderedDict()
        for pos, valor in enumerate(reg):
            llave = cabeceras[pos]
            aux[llave] = valor
        resultados.append(aux)
    return resultados

def registros_con_nombre_02(cabeceras, registros):
    # return map(lambda reg: OrderedDict(zip(cabeceras,reg)), datos)
    return [OrderedDict(zip(cabeceras,reg)) for reg in registros]

def reg_match(registro, condiciones):
    """
    Devuelve True si TODOS las condiciones expresadas
    en el diccionario 'condiciones' son cumplidas por
    el registro de tipo diccionario de la variable
    'registro'.

    Ej.
    registro = {'a': '10', 'b':'20', 'c':'30'}
    condiciones = {'b': '20', 'c': '40'}
    reg_match(registro, condiciones) # False
    condiciones = {'c': '30', 'a': '10'}
    reg_match(registro, condiciones) # True
    """
    for campo, valor in condiciones.iteritems():
        try:
            if registro[campo] != valor:
                return False
        except KeyError:
                return False
    return True

def csv_select(campos='*', csvpath='datos.csv', condiciones={}):
    """
    Para simular algo como:

    SELECT codigo, nombre, nombre, codigo WHERE nombre='Juan' AND codigo='10'

    campos = ['codigo','codigo','nombre','nombre']
    tabla  = 'peliculas.csv'
    condiciones = {'nombre':'Juan', 'codigo':'10'}

    csv_select(campos, tabla, condiciones)

    Devuelve algo como:

    [
        ('codigo', '1'),
        ('codigo', '1'),
        ('nombre', 'Peter Pan'),
        ('nombre','Peter Pan')
    ]
    """
    resultados = []
    cabeceras, datos = cargar_csv(csvpath).values()
    registros = registros_con_nombre(cabeceras, datos)
    for reg in registros:
        if reg_match(reg, condiciones):
            if campos == '*':
                resultados.append(reg.items())
            else:
                aux = []
                for camp in campos:
                    aux.append( (camp, reg[camp]) )
                resultados.append(aux)
    return resultados


if __name__ == '__main__':
    cabeceras, datos = cargar_csv('peliculas.csv').values()
    # En caso el diccionario no fuera ordenado
    # aux = cargar_csv('peliculas.csv')
    # cabeceras = aux['cabeceras']
    # datos = aux['datos']
    #registros = registros_con_nombre(cabeceras, datos)
    campos = '*'
    tabla = 'peliculas.csv'
    condiciones = {'codigo':'1', 'nombre': 'Terminator X'}
    registros = csv_select(campos, tabla, condiciones)
    #pprint.pprint(registros)
    print json.dumps(registros, indent=4)
