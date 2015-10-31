import random

def getDiaDeSemana(n):
    if n==1:
        return 'Lunes'
    elif n==2:
        return 'Martes'
    elif n==3:
        return 'Miercoles'
    elif n==4:
        return 'Jueves'
    return '---'

def decDiaDeSemana(funcionDecorada):
    def aux():
        numero = funcionDecorada()
        dia = getDiaDeSemana(numero + 1)
        return '%s: %s' % (numero, dia)
    return aux

@decDiaDeSemana
def numeroEntre1y3():
    numero = random.randint(1,3)
    return numero

for i in range(7):
    print numeroEntre1y5()
