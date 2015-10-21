# -*- coding: utf8 -*-

class Contador(object):

    def __init__(self):
        self.cuenta = 0
        self.incremento = 1

    def incrementar(self):
        self.cuenta += self.incremento

class Contador2(Contador):

    def __init__(self, cuenta=0, *args, **kwargs):
        super(Contador2, self).__init__(*args, **kwargs)
        self.cuenta = cuenta

class Contador3(Contador2):

    def __init__(self, cuenta=0, incremento=1, *args, **kwargs):
        super(Contador3, self).__init__(cuenta, *args, **kwargs)
        self.incremento = incremento


if __name__ == '__main__':

    contador1 = Contador()
    print contador1.cuenta

    contador2 = Contador2(cuenta=10)
    print contador2.cuenta

    contador3 = Contador3(cuenta=1000, incremento=100)
    contador3.incrementar()
    print contador3.cuenta
