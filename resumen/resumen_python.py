#!/usr/bin/env python
# -*- coding: utf8 -*-

########################################################################
##                                                                    ##
##      RESUMEN DE PYTHON: CURSO DE PYTHON Y DJANGO PARA EL IGP       ##
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

# Sin embargo, una camino completamente distinto que podríamos seguir
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

# Obsérvese con mucha atención como el parámetro "f" de la función
# "operando_pares" a pesar de no haber sido definida como parámetro o
# variable local de la función "aux" se encuentra definida en el
# momento de la defición de la función "aux" y por lo tanto puede ser
# utilizada, construyéndose una "cerradura" o "closure".

suma = operandos_pares(suma)

assert suma(2,2) == 4
assert suma(1,3) is None

# Vamos a volver a escribir el decorador para que la estrategia sea
# un poco más genérica y funcione no solo con dos parámetros llamados
# a y b sino con cualquier cantidad de parámetros sin importar si fueron
# pasados por posición o por nombre de argumento.

def operandos_pares(f):
    def aux(*args, **kwargs):
        for v in args:
            if type(v) in [int, float] and v % 2 != 0:
                return None
        for k,v in kwargs.iteritems():
            if type(v) in [int, float] and v % 2 != 0:
                return None
        return f(*args, **kwargs)
    return aux

# La nueva versión de suma ahora hace exactamente eso: devuelve la suma
# de dos números si estos son AMBOS divisibles por dos ó devuelve None
# en caso de que al menos uno de ellos no lo fuera.

def suma_de_parametros(*args):
    return sum(args)

suma_de_parametros = operandos_pares(suma_de_parametros)
assert suma_de_parametros(2, 4, 6, 8) == 20
assert suma_de_parametros(2, 4, 6, 9) == None

# ¿Que tál si ahora quisiéramos la misma funcionalidad en la resta?

def resta(a, b):
    return a - b

# En vez de escribir una versión especializada de la función resta lo
# que tenemos que hacer es una vez más componer la función y envolverla
# con otra que implemente la lógica deseada.

# Ya tenemos escrito el decorador "operandos_pares" así que simplemente
# lo reutilizamos:

resta = operandos_pares(suma)

# Uno de los resultados interesantes de seguir este enfoque es que no
# necesariamente tenemos que modificar las funciones originales sino que
# podemos obtener versiones alternativas construídas decorando funciones
# pre-existentes con decoradores disponibles.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

suma_solo_pares = operandos_pares(suma)
resta_solo_pares = operandos_pares(resta)

assert suma(1,3) == 4
assert suma_solo_pares(1,3) == None

# Ahora, no perdámos de vista que POR DEFINICIÓN un decorador SOLO puede
# recibir una función y devolver una función. El decorador por ejemplo
# NO podría recibir un parámetro como el valor por omisión a devolver
# en caso de que ambos operandos NO fueran pares.

# Para poder simular, OJO, simular el hecho de poder pasar parámetros
# a un decorador, lo que vamos a hacer es definir el decorador dentro
# de otra función que no tenga las mismas restricciones en relación a
# la cantidad y semántica de sus parámetros y hacer que estos parámetros
# esten disponibles dentro del decoradores via un closure.

def operandos_pares(valor_por_omision=None):
    def decorador(f):
        def aux(*args, **kwargs):
            for v in args:
                if type(v) in [int, float] and v % 2 != 0:
                    return valor_por_omision
            for k,v in kwargs.iteritems():
                if type(v) in [int, float] and v % 2 != 0:
                    return valor_por_omision
            return f(*args, **kwargs)
        return aux
    return decorador

# Con esta nueva implementación, debemos primero invocar a la función
# que crea y personaliza el decorador dinámicamente y luego utilizar
# el decorador obtenido para decorar nuestra función.

decorador = operandos_pares(valor_por_omision=0)
suma = decorador(suma)

assert suma(2,2) == 4
assert suma(1,3) == 0

# Esto también se hubiera podido hacer en un solo paso como sigue:

def suma(a, b):
    return a + b

suma = operandos_pares(valor_por_omision=0)(suma)

# Python ofrece una sintaxis alternativa y bastante útil para decorar
# una función al momento de definirla.

@espejo
def suma(a, b):
    return a + b

assert suma(5, 3) == 8

@operandos_pares(valor_por_omision=0)
def suma(a, b):
    return a + b

assert suma(2, 2) == 4
assert suma(3, 5) == 0

# Los decoradores pueden anidarse también:

@espejo
@operandos_pares(valor_por_omision=0)
def suma(a, b):
    return a + b

# Es semánticamente equivalente a escribir:

suma = espejo(operandos_pares(valor_por_omision=0)(suma))
