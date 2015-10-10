import sys
import random
import string

# Detectamos uso correcto
if (len(sys.argv) != 2) or not sys.argv[1].isdigit():
    exit('Uso:\tlicencias_windows n\nn\tEs un numero entero positivo')

# Funcion para generar 1 licencia
def generate():
    VALIDCHARS = string.ascii_uppercase + string.digits
    partes = []
    for i in range(5):
        parte = []
        for j in range(5):
            parte.append(random.choice(VALIDCHARS))
        partes.append(''.join(parte))
    return '-'.join(partes)

# obteniendo el parametro por consola
n = int(sys.argv[1])

# validando que las licencias generadas sean unicas
licencias = set([])
while len(licencias) < n:
    licencias.add(generate())

# imprimiendo las licencias unicas generadas
print '\n'.join(licencias)

