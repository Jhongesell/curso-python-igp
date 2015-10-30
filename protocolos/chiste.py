#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Estamos inventando un protocolo para contar chistes.
Todos las las clases que implementen el método mágico
__chiste__(self) podrán devolver una cadena con el
cuerpo de un chiste y si no están inspirados podrán
levantar una excepción del tipo NoEstoyInspirado con
la explicación pertinente.
"""

import random

class NoEstoyInspirado(Exception):
    pass


def chiste(obj):
    return obj.__chiste__()


class Melcochita(object):

    def __chiste__(self):
        return u"¡No vayan!"


class Cavallini(object):

    def __chiste__(self):
        return u"¡Ay que rico!"


class ComicoAmbulante(object):

    def __chiste__(self):
        dado = random.randint(1, 6)
        if dado % 2 == 0:
            raise NoEstoyInspirado('Ahorita no se me ocurre nada')
        else:
            return u"Contando algún chiste..."


if __name__ == '__main__':

    melco = Melcochita()
    print chiste(melco)

    cavallini = Cavallini()
    print chiste(cavallini)

    comico = ComicoAmbulante()

    while True:
        print chiste(comico)
