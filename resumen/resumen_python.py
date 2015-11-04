#!/usr/bin/env python
# -*- coding: utf8 -*-

########################################################################
##                                                                    ##
##       RESUMEN DE PYTHON: CURSO DE PYTHON Y DJANGO PARA EL IGP      ##
##                                                                    ##
########################################################################

########################################################################
## 01. HISTORIA                                                       ##
########################################################################

# Algunos puntos relevantes sobre la historia de Python:
#
# 01. Creado por Guido von Rossum

########################################################################
## 00. SINTAXIS BÁSICA                                                ##
########################################################################

########################################################################
## 00. TIPOS DE DATOS BÁSICOS                                         ##
########################################################################

########################################################################
## 00. DECORADORES                                                    ##
########################################################################

# Un decorador no es otra cosa que una simple función que recibe como
# ÚNICO parámetro un objeto ejecutable (callable) como una función y
# devuelve otro objeto ejecutable.
#
# La idea de los decoradores es poder extender la funcionalidad de un
# objeto ejecutable componiéndolo con otras funciones.

# El decorador más simple sería la función "espejo"

def espejo(obj):
    """Devuelve el mismo objeto Python que se pasa como parámetro"""
    return obj

# Ahora definamos una función cualquiera:

def suma(a, b):
    return a + b

# Podemos "decorar" esta función redefiniéndola como la salida de la
# función decorador pasando el antiguo valor de la función a decorar
# como su argumento.

suma = espejo(suma)

# En este caso el objeto asignado al identificador "suma" sigue siendo
# el mismo y la funcionalidad no ha sido alterada para nada.
assert suma(1,1) == 2

# Pero ¿que tal si quisiéramos que solo sea posible sumar dos números
# si ambos son pares? Lo que muchos programadores harían es simplemente
# crear una nueva función con esta condición escrita como parte de
# la función.

# La nueva versión quedaría, por ejemplo, de esta manera:

def suma(a, b):
    if (a % 2 == 0) and (b % 2 == 0):
        return a + b

# Esta nueva versión de la función, efectivamente, solo devuelve la suma
# de ambos sumandos si es que los dos son divisibles entre dos.

# Sin embargo, una camino completamente distinto que podrías seguir
# sería el de dejar la función original tal y como estaba:

def suma(a, b):
    return a + b

# para luego crear un decorador que solo la invoque si se cumple la
# condición esperada. Así por ejemplo:

def operandos_pares(f):
    def aux(a, b):
        if (a % 2 == 0) and (b % 2 == 0):
            return f(a, b)
    return aux

suma = operandos_pares(suma)

assert suma(2,2) == 4
assert suma(1,3) is None

# La nueva versión de suma ahora hace exactamente eso: devuelve la suma
# de dos números si estos son AMBOS divisibles por dos ó devuelve None
# en caso de que al menos uno de ellos no lo fuera.

# ¿Que tál si ahora quisiéramos la misma funcionalidad en la resta?

def resta(a, b):
    return a - b

# En vez de escribir una versión especializada de la función resta lo
# que tenemos que hacer es una vez más componer la función y envolverla
# con otra que implemente la lógica deseada.

# Ya tenemos escrito el decorador "operandos_pares" así que simplemente
# lo reutilizamos:

resta = operandos_pares(suma)

