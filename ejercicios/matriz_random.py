import random

listagrande = [random.randint(0,100) for x in range(1,1000)]
listadelistas = []
lista = []
for i,r in enumerate(listagrande):
    lista.append(r)
    if((i+1)%100==0):
        listadelistas.append(lista)
        lista = []

print listadelistas

