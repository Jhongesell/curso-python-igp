# -*- coding: utf8 -*-

class Alumno0():
    pass

class Alumno(object):
    pass

class Alumno2(object):

    nombre = 'Juan'

    def saludar(self):
        print "Hola, me llamo %s" % self.nombre

class Alumno3(object):

    def __init__(self, n, a):
        self.nombre = nombre
        self.apellido = apellido

class Alumno4(object):

    def __init__(self, **kwargs):
        kwargs.setdefault('edad', 10)
        for k in kwargs:
            setattr(self, k, kwargs[k])

class Alumno5(object):

    def __init__(self, nombre='Pepe'):
        self.nombre = nombre
        self.edad = 10

if __name__ == '__main__':

    obj = Alumno2()
    obj.saludar()
