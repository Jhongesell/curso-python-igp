#!/usr/bin/env python
# -*- coding: utf -*-

import random

def llamar_aveces(f):
    def aux(*args, **kwargs):
        if random.choice([True, False]):
            f(*args, **kwargs)
    return aux


def llamar_n_veces(n):
    def decorador(f):
        def aux(*args, **kwargs):
            for x in range(n):
                f(*args, **kwargs)
        return aux
    return decorador

@llamar_aveces
@llamar_n_veces(10)
def saludar():
    print "Hola"

if __name__ == '__main__':
    print "Llamando a saludar..."
    saludar()
