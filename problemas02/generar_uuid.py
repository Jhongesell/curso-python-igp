#!/usr/bin/env python
# -*- coding: utf8 -*-

import random


def genhexchar():
    '''
    Genera un caracter hexadecimal aleatoriamente
    '''
    hexchars = [str(x) for x in range(10)]
    hexchars.extend(['a', 'b', 'c', 'd', 'e', 'f'])
    return random.choice(hexchars)

def genhexserie(n):
    '''
    Genera una serie de n caracteres hexadecimales aleatorios
    '''
    ret = ''
    for i in range(n):
        ret += genhexchar()
    return ret

def generar_uuid(lens):
    series = []
    for i in lens:
        series.append(genhexserie(i))
    return '-'.join(series)

print generar_uuid([8, 4, 4, 4, 12])
