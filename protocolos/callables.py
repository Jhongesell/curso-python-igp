#!/usr/bin/env python
# -*- coding: utf8 -*-

class Sumadora(object):

    def __init__(self, numero):
        self.numero = numero

    def __call__(self, x):
        return x + self.numero

if __name__ == '__main__':

    sumadora_de_cincos = Sumadora(5)
    print sumadora_de_cincos(10)
    print sumadora_de_cincos(100)
    print sumadora_de_cincos(0)
