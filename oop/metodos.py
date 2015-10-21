# -*- coding: utf8 -*-

class Contador(object):

    def __init__(self):
        self.cuenta = 0
        self.incremento = 1

    @staticmethod
    def incrementar_cantidad(cantidad, incremento):
        return cantidad + incremento

    @classmethod
    def imprimir_tipo_contador(cls):
        print cls.__name__

    def incrementar(self):
        self.cuenta += self.incremento

class Contador2(Contador):
    pass

if __name__ == '__main__':
    print Contador.incrementar_cantidad(10, 1) # 11
    Contador.imprimir_tipo_contador()
    Contador2.imprimir_tipo_contador()
