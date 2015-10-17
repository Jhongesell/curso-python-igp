#!/usr/bin/env python
# -*- coding: utf -*-

def saludar():
    print "Hola"

def llamar_n_veces(n):
    def decorador(f):
        def aux(*args, **kwargs):
            for x in range(n):
                f(*args, **kwargs)
        return aux
    return decorador

if __name__ == '__main__':
    saludar_x_2 = llamar_n_veces(2)(saludar)
    saludar_x_4 = llamar_n_veces(2)(saludar_x_2)
    print "Llamando a saludar..."
    saludar()
    print "Llamando a saludar_x_2..."
    saludar_x_2()
    print "Llamando a saludar_x_4..."
    saludar_x_4()
