#!/usr/bin/env python
# -*- coding: utf8 -*-

class Almacen(object):

    def __init__(self, cosas):
        self.cosas = cosas
        self.apuntador = 0

    def next(self):
        if self.apuntador < len(self.cosas):
            aux = self.cosas[self.apuntador]
            self.apuntador += 1
            return aux
        else:
            raise StopIteration(u'Se me acabaron!!')

    def __iter__(self):
        #return iter([1, 2, 3])
        return self

if __name__ == '__main__':
    almacen = Almacen(['martillo', 'desarmador', 'wincha'])
    for cosa in almacen:
        print cosa
