from random import randint as entero_aleatorio

def suma(valor_inicial=0, *args):
    return reduce(lambda a,b: a + b, args, valor_inicial)

if __name__ == '__main__':
    assert suma(1, 1, 1) == 3
