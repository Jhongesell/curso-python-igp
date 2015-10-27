#!/usr/bin/env python
# -*- coding: utf8 -*-


def triangulo_pascal(n, pascal=[]):

    def imprimir(pascal):
        def imprimirfila(fila):
            return ('    '.join(map(lambda x: str(x), fila)))
        base = imprimirfila(pascal[-1]).__len__()
        for fila in pascal:
            txtfila = imprimirfila(fila)
            prefix = ' ' * ( (base - txtfila.__len__()) / 2 )
            print prefix + txtfila

    if (len(pascal)==n):
        return imprimir(pascal)

    if len(pascal)==0:
        pascal = [[1]]
    elif len(pascal)==1:
        pascal = [[1],[1,1]]
    else:
        nueva_fila = [1]
        ultima_fila = pascal[-1]
        for k,v in enumerate(ultima_fila[:-1]):
            nueva_fila.append(v + ultima_fila[k+1])
        nueva_fila.append(1)
        pascal.append(nueva_fila)

    return triangulo_pascal(n, pascal)

triangulo_pascal(8)