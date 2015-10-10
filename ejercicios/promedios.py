#!/usr/bin/env python
# -*- coding: utf8 -*-
# promedio de notas
__author__ = 'hubergilt@hotmail.com'
__name__='promedio'

def preguntar(pregunta=None, funcion=None, errmsg=None):
    if pregunta is None:
        pregunta = ''
    if len(pregunta) > 0:
        pregunta += ': '
    if funcion is None:
        funcion = str
#    if errmsg is None:
#        errmsg = 'Valor \'%s\' invalido'

    respuesta = raw_input(pregunta)
    try:
        valor = funcion(respuesta)
        print valor
    except ValueError, e:
        if errmsg is None:
            print e.message
        else:
            print errmsg % respuesta



#preguntar('Ingrese una nota entre 0.0 y 20.0', float, '!El valor \'%s\' no es un número válido!')
#preguntar()
#preguntar('Esta seguro?', lambda x: x.lower()=='si', 'Mal ! %s ')
def validarSexo(val):
    if val.lower() in ['m','f']:
        return val
    else:
        raise ValueError('Valor \'%s\' no es un genero valido')
preguntar('Sexo',  validarSexo)
#preguntar('Esta seguro?', int, 'Mal ! %s ')
exit()








titulo='*CALCULO DE PROMEDIO DE NOTAS*'
print '*' * len(titulo)
print titulo
print '*' * len(titulo)

suma=0
cont=0
while True:
    texto=raw_input('Ingrese una nota entre 0.0 y 20.0: ')
    try:
        nota=float(texto)
        if 0.0<=nota<=20.0:
            suma+=nota
            cont+=1
            while True:
                texto=raw_input('Desea ingresar otra nota (S/N)? ')
                if texto.strip().lower() in ('si','s','no','n'):
                    break
                else:
                    print 'Las respuestas válidas son: "s", "n", "S", "N", "si", "no", "SI", "NO", "Si" y "No"'
            if texto.strip().lower() in ('no','n'):
                break
        else:
            print '!El valor \'%s\' se encuentra fuera del rango permitido!' % texto
    except ValueError:
        print '!El valor \'%s\' no es un número válido!' % texto  
        continue

try:
    promedio = suma/float(cont)
    print 'Se ingresaron \'%s\' notas y el promedio es %.2f (%s)' % (cont, promedio, 'APROBADO' if promedio>=10.5 else 'DESAPROBADO')
except ZeroDivisionError:
    print 'No se puede dividir entre cero'