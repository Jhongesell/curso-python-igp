#!/usr/bin/env python
# -*- coding: utf -*-

def saludar():
    print "Hola"

def llamar_dos_veces(f):
    def aux(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)
    return aux

if __name__ == '__main__':
    saludar_x_2 = llamar_dos_veces(saludar)
    saludar_x_4 = llamar_dos_veces(saludar_x_2)
    print "Llamando a saludar..."
    saludar()
    print "Llamando a saludar_x_2..."
    saludar_x_2()
    print "Llamando a saludar_x_4..."
    saludar_x_4()

