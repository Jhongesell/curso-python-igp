#!/usr/bin/env python
# -*- coding: utf -*-

def resta(a, b):
    return a - b

def reemplazar_por_suma(f):
    def suma(a, b):
        return a + b
    return suma

if __name__ == '__main__':
    resta = reemplazar_por_suma(resta)
    print resta(10, 10)

    #def recibir_algo_y_devolver_20(x):
    #    return 20

    #a = 10
    #a = recibir_algo_y_devolver_20(a)
    #print a
