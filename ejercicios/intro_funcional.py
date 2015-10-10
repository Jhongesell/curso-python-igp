# Filtrar:
# Lista de numeros del 1 al 100 que sean multiplos de 7

def filtrar(valores, filtro):
    valores_validos = []
    for i in valores:
        if filtro(i):
            valores_validos.append(i)
    return valores_validos

# print filtrar([1,8,10,11,2,3,4,5,6], lambda x: x%3==0)
# [2, 4, 6]

#def esMultiploDe7(valor):
#    return valor%7==0
#multiplos7 = filtrar(range(1,100+1), esMultiploDe7)

multiplos7 = filtrar(range(1,100+1), lambda x: x%7==0)
#print multiplos7


# Mapear
# Lista de los cubos de los numeros del 1 al 100 que sean multiplos de 7

def mapear(valores, fmapeo):
    nuevos_valores = []
    for i in valores:
        nuevos_valores.append(fmapeo(i))
    return nuevos_valores

#print mapear([1,2,4,10], lambda x: x**4)

cubos = mapear(multiplos7, lambda x: x**3)
#for i in multiplos7:
#    cubos.append(i**3)

#print cubos





# Reduccion
# Sumatoria de la Lista de los cubos de los numeros del 1 al 100 que sean multiplos de 7
def reducir(valores, inicial, funcion):
    for i, valor in enumerate(valores):
        if i == 0:
            parcial = funcion(inicial, valor)
        else:
            parcial = funcion(parcial, valor)
    return parcial

#print reducir([1, 2, 3, 4, 5], 0, lambda x, y: x + y) # 15
#print reducir([1, 2, 3, 4, 5], 1, lambda x, y: x * y) # 120


#sumatoria = 0
#for i in cubos:
#    sumatoria += i

sumatoria = reducir(cubos, 0, lambda x, y: x + y)
#print sumatoria




# resumen:

multiplos7 = filtrar(range(1,100+1), lambda x: x%7==0)
cubos = mapear(multiplos7, lambda x: x**3)
sumatoria = reducir(cubos, 0, lambda x, y: x + y)


print reducir(mapear(filtrar(range(1,100+1), lambda x: x%7==0), lambda x: x**3), 0, lambda x, y: x + y)

cadena = 'Contar los valores de esta cadena++'
print reducir(mapear(cadena, lambda x: 1), 0, lambda x, y: x+y)

cadenas = ['uno', 'dos', 'tres', 4]
#print ''.join(cadenas)

#print reducir(cadenas,'', lambda x,y: str(x) + str(y) )
print reducir(mapear(cadenas, lambda x: str(x)),'', lambda x,y: x + y )

cadena = '   JUAN perez    RoDrIgUez '
lista = cadena.split(' ')
lista_limpia = filter(lambda x: len(x)>0, cadena.split(' '))
lista_formateada = map(lambda x: x.lower().capitalize(), lista_limpia)
espaciada = map(lambda x: x + ' ', lista_formateada)
concatenada = reduce(lambda x, y: x + y,espaciada, '')
print "'%s'" % concatenada

#print reduce(lambda x, y: x )
# Juan Perez Rodrigez

print [x**3 for x in range(5) if x%2==0 ]

print [x.strip().split(',') for x in open('funciones_cine.csv').readlines() if len(x.strip())>0 ]


nombres = ['Juan Perez', 'Carlos Garcia', 'Ernesto Cuadros', 'Antonio  ']
# ['PEREZ, Juan', ...]

formatear = lambda x: '%s, %s' % (x.split(' ')[1].upper(), x.split(' ')[0])
conservar = lambda x: len(x.strip().split(' '))>1

print [formatear(x) for x in nombres if conservar(x)]

zzip = lambda lst1, lst2: [(x,y) for x in lst1 for y in lst2 ]

print [(x,y) for x in range(7) for y in range(7) if abs(x-y)<2 ]
print zzip([1,2,3], [6,7,8])

print ord('$')
print chr(65)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
print ''.join([chr(x) for x in range(ord('A'), ord('Z')+1)])

import random

print [random.randint(0,10000) for x in range(10)]

numeros = []
for i in range(10):
    numeros.append(random.randint(0,10000))
print numeros