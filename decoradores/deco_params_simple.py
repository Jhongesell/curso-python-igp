def sumar_dos(x):
    return x+2

def crear_sumadora(n):
    def sumadora(x):
        return x+n
    return sumadora

sumar_uno = crear_sumadora(1)
sumar_dos = crear_sumadora(2)

print sumar_uno(18)
print sumar_dos(18)

def decoSiempreUno(funcion_a_decorar):
    def aux(*args, **kwargs):
        return 1
    return aux

@decoSiempreUno
def algo():
    pass

print algo()

def decoSiempreEsteValor(valor):
    def decoSiempreValor(funcion_a_decorar):
        def aux(*args, **kwargs):
            return valor
        return aux
    return decoSiempreValor

@decoSiempreEsteValor(55)
def suma(a,b):
    return a+b

print 'suma'
print suma(10,20)