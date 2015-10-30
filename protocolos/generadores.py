#!/usr/bin/env python
# -*- coding: utf8 -*-

# El comando "yield" es un "return" que recuerda donde se quedó
# en la llamada anterior. La función no devuelve directamente el
# valor como con "return" sino que devuelve un objeto iterable que
# se llama "generador"

def del_uno_al_tres():
    yield 1
    yield 2
    yield 3

if __name__ == '__main__':
    g = del_uno_al_tres()
    try:
        while True:
            print g.next()
    except StopIteration:
        pass

    for elem in del_uno_al_tres():
        print elem
