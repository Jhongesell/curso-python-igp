# -*- coding: utf8 -*-

class Alumno(object):

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print "Hola me llamo %s" % self.nombre


def asignar_nombre(objeto, nombre):
    objeto.nombre = nombre


def saludar(objeto):
    print "Hola me llamo %s" % objeto.nombre

atributos = {'__init__': asignar_nombre, 'saludar': saludar}
Alumno2 = type('Alumno2', (object,), atributos)

if __name__ == '__main__':

    obj1 = Alumno(nombre='Juan')
    obj1.saludar() # Imprime "Hola me llamo Juan"

    obj2 = Alumno2(nombre='Pedro')
    obj2.saludar() # Imprime "Hola me llamo Pedro"

    # Imprime "Hola me llamo Marcos"
    (type('Alumno2', (object,), atributos))(nombre='Marcos').saludar()
