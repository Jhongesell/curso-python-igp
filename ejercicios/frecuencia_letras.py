# -*- coding: utf8 -*-
import sys
import string

# Detectamos uso correcto
if (len(sys.argv) != 2):
    exit('Uso:\tfrecuencia_letras cadena\ncadena\tEs una frase')

cadena = sys.argv[1]
#alfabeto = list(u'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'.encode('utf-8'))
alfabeto = list(string.ascii_uppercase)


for a in alfabeto:
    print "%s -> %d" % (a , cadena.upper().count(a))