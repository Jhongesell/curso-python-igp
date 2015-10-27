#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

if len(sys.argv)!=3:
    msg = 'Uso: ' + sys.argv[0] + ' min max\n'
    exit(msg)

try:
    min = int(sys.argv[1])
    max = int(sys.argv[2])
except ValueError:
    exit('"%s" y "%s" debe ser un entero' % (sys.argv[1], sys.argv[2]))


def capicua(n):
    def invertir_cadena(cadena_inicial, cadena_final=''):
        if cadena_inicial == '':
            return cadena_final
        cabeza = cadena_inicial[:1]
        cola = cadena_inicial[1:]
        return invertir_cadena(cola, cabeza + cadena_final)
    return str(n)==invertir_cadena(str(n))

capicuas = []
for i in range(min, max):
    if capicua(i):
        capicuas.append(str(i))

print ' '.join(capicuas)