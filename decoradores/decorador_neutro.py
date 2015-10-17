#!/usr/bin/env python
# -*- coding: utf -*-

def suma(a, b):
    return a + b

def decorador_neutro(f):
    def aux(*args, **kwargs):
        #f(1, 2, 3, x=10, y=20, z=30)
        #por_posicion = (1, 2, 3)
        #por_nombre = {'x': 10, 'y': 20, 'z':30}
        #f(*por_posicion, **por_nombre)
        return f(*args, **kwargs)
    return aux

def decorador_no_tan_neutro(f):
    def aux(*args, **kwargs):
        if 'b' in kwargs:
            kwargs['b'] = 1000
        return f(*args, **kwargs)
    return aux

if __name__ == '__main__':
    suma_decorada = decorador_neutro(suma)
    print suma_decorada(10, b=10)
