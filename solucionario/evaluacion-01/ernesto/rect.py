#!/usr/bin/env python
# -*- coding: utf8 -*-

class ErrorDeRectangulo(Exception):
    pass

class Rectangulo:

    def __init__(self, alto, ancho):
        if not isinstance(alto, int):
            raise ErrorDeRectangulo('alto debe ser entero')
        if alto <= 0 :
            raise ErrorDeRectangulo('alto debe ser mayor o igual a 1')
        if not isinstance(ancho, int):
            raise ErrorDeRectangulo('ancho debe ser entero')
        if ancho <= 0 :
            raise ErrorDeRectangulo('ancho debe ser mayor o igual a 1')
        self.alto = alto
        self.ancho = ancho




testcases = [
    ['',1,ErrorDeRectangulo,'alto debe ser entero'],
    [-1,1,ErrorDeRectangulo,'alto debe ser mayor o igual a 1'],
    [1,'',ErrorDeRectangulo,'ancho debe ser entero'],
    [1,-1,ErrorDeRectangulo,'ancho debe ser mayor o igual a 1'],
]

for test in testcases:
    try:
        r = Rectangulo(test[0],test[1])
    except Exception as e:
        assert isinstance(e, test[2])
        assert e.message==test[3]