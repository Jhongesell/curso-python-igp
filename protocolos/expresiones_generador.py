#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Las expresiones de generador son idénticas a las listas por
comprensión con la diferencia de que en ver de devolver listas
devuelven generadores.
"""

if __name__ == '__main__':

    print u"Cuadrados de los números del 1 al 10\n"

    ge = (n**2 for n in xrange(1, 10 + 1))
    try:
        while True:
            print ge.next()
    except StopIteration:
        pass

    print u"\nCubos de los números del 1 al 10\n"

    for cubo in (n**3 for n in xrange(1, 10 + 1)):
        print cubo
