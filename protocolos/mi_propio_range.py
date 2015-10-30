#!/usr/bin/env python
# -*- coding: utf8 -*-

def mi_propio_range(n):
    lista = []
    i = 0
    while i < n:
        lista.append(i)
        i += 1
    return lista

def mi_propio_xrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

if __name__ == '__main__':
    for x in mi_propio_range(3):
        print x
    for x in mi_propio_xrange(3):
        print x
