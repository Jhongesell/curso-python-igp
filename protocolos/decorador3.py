import random

def parche_aleatorio(*funciones):
    def decorador(f):
        def aux(*args, **kwargs):
            f = random.choice(funciones)
            print "Estoy invocando a %s" % f
            return f(*args, **kwargs)
        return aux
    return decorador

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

@parche_aleatorio(suma, resta, multiplica)
def divide(a, b):
    return a / b

if __name__ == '__main__':
    print divide(10, 10)
