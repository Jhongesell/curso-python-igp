#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

if len(sys.argv)!=2:
    msg = 'Uso: ' + sys.argv[0] + ' "Cadena a invertir"\n'
    exit(msg)


def invertir_cadena(cadena_inicial, cadena_final=''):
    if cadena_inicial == '':
        return cadena_final
    cabeza = cadena_inicial[:1]
    cola = cadena_inicial[1:]
    return invertir_cadena(cola, cabeza + cadena_final)

print invertir_cadena(sys.argv[1])
