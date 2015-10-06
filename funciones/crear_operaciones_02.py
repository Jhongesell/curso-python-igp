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
    signo, arg1, arg2 = sys.argv[1:4]
    operacion = crear_operacion(signo)
    try:
        print operacion(float(arg1), float(arg2))
    except ValueError:
        pass
