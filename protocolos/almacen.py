#!/usr/bin/env python
# -*- coding: utf8 -*-

class YaNoTengoMasCosas(Exception):
    pass

class Almacen(object):

    def __init__(self, cosas):
        self.cosas = cosas
        self.apuntador = 0

    def dame(self):
        if self.apuntador < len(self.cosas):
            aux = self.cosas[self.apuntador]
            self.apuntador += 1
            return aux
        else:
            raise YaNoTengoMasCosas(u'Se me acabaron!!')

if __name__ == '__main__':
    almacen = Almacen(['martillo', 'desarmador', 'wincha'])
    try:
        while True:
            print almacen.dame()
    except YaNoTengoMasCosas:
        pass

