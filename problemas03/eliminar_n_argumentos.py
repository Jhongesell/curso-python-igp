#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

def eliminar_n_argumentos(f):
    def aux(*args, **kwargs):
        if len(args)<2:
            exit('USO: %s n a b c ...' % args[0])
        try:
            n = int(sys.argv[1])
        except ValueError:
            exit('"%s" debe ser un entero' % sys.argv[1])

        if n > len(args) - 2:
            exit('Faltan argumentos para borrar')
        args = args[2+n:]
        f(*args, **kwargs)
    return aux

@eliminar_n_argumentos
def imprimir_argumentos(*args, **kwargs):
    print "Argumentos por posición:"
    print args
    print "Argumentos por nombre:"
    print kwargs


imprimir_argumentos(*sys.argv)