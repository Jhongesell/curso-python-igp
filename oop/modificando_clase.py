# -*- coding: utf8 -*-

class Alumno(object):

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print "Hola me llamo %s" % self.nombre

class Alumno2(object):
    pass

def asignar_nombre(objeto, nombre):
    objeto.nombre = nombre

def saludar(objeto):
    print "Hola me llamo %s" % objeto.nombre

Alumno2.__init__ = asignar_nombre
Alumno2.saludar = saludar

if __name__ == '__main__':

    obj1 = Alumno(nombre='Juan')
    obj1.saludar() # Imprime "Hola me llamo Juan"

    obj2 = Alumno2(nombre='Pedro')
    obj2.saludar() # Imprime "Hola me llamo Pedro"
