#!/usr/env/bin python
# -*- coding: utf8 -*-

class Persona(object):

    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])

if __name__ == '__main__':

    persona1 = Persona(
        nombre='Juan Perez',
        edad=50,
        ocupacion='abogado'
    )

    persona2 = Persona(
        nombre='Juan Perez Jr.',
        edad=20,
        ocupacion='estudiante',
        padre=persona1
    )

    print persona2.padre.nombre
