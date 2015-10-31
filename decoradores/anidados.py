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
    elif n==5:
        return 'Viernes'
    return '---'

def decoGetDiaSemana(funcionDecorada):
    #print '-> D'
    def aux():
        #print '-> E'
        return getDiaDeSemana(funcionDecorada()) + ' <-- '
    return aux

def cambiarNumero(n):
    return n*2 - 1

def decoCambiarNumero(funcionDecorada):
    #print '-> B'
    def aux():
        #print '-> C'
        return cambiarNumero(funcionDecorada())
    return aux


@decoGetDiaSemana
@decoCambiarNumero
def numeroEntre1y3():
    #print '-> A'
    numero = random.randint(1,3)
    return numero


# sumarMil ( duplicar( generarAleatorio(1,10) ) )

#print numeroEntre1y3()
#exit()

for i in range(5):
    print numeroEntre1y3()
    #print getDiaDeSemana(numeroEntre1y3())
    #print getDiaDeSemana(cambiarNumero(numeroEntre1y3()))