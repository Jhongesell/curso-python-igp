#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

def crear_operacion(signo):
    if signo == '+':
        def temp(arg1, arg2):
            return arg1 + arg2
        return temp
    elif signo == '-':
        def temp(arg1, arg2):
            return arg1 - arg2
        return temp

if __name__ == '__main__':
    operacion = crear_operacion('+')
    print operacion(1,1)

    operacion = crear_operacion('-')
    print operacion(1,1)

    operacion = crear_operacion('*')
    if operacion is not None:
        print operacion(1, 1)

    try:
        operacion = crear_operacion('/')
        print operacion(1, 1)
    except TypeError:
        pass
