#!/usr/bin/env python
# -*- coding: utf8 -*-

def inspeccionar_argumentos(f):
    def aux(*args, **kwargs):
        print 'Argumentos por posición:'
        print args
        print 'Argumentos por nombre:'
        print kwargs
        return f(*args, **kwargs)
    return aux

@inspeccionar_argumentos
def suma(a, b):
    return a + b


@inspeccionar_argumentos
def subrayar(texto, caracter='*'):
    print texto
    print caracter * len(texto)


print suma(1,1)
print
subrayar('Hola mundo')