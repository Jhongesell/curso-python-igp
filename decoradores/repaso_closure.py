#!/usr/bin/env python
# -*- coding: utf -*-

a = 10
print id(a)

def imprimir_a():
    print id(a)
    print a

if __name__ == '__main__':
    imprimir_a()
    a = 20
    imprimir_a()
    print "a: %d" % a
