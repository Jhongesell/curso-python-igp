#!/usr/bin/env python
# -*- coding: utf -*-

def crear_sumadora(n):
    def aux(x):
        return x + n
    return aux

if __name__ == '__main__':
    sumadora_de_cincos = crear_sumadora(5)
    print sumadora_de_cincos(10)
    # concatenadora_de_hola = crear_sumadora("Hola")
    # print concatenadora_de_hola("Amigo ")
