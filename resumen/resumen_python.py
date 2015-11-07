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

# ==> ANTONIO <==

# Algunos puntos relevantes sobre la historia de Python:
#
# 01. Creado por Guido von Rossum

########################################################################
## 00. SINTAXIS BÁSICA                                                ##
########################################################################

# En Python se espera que cada sentencia ocupe una línea.
# Sin embargo, es posible colocar dos o más sentencias en una
# sola línea separándolas por punto y coma.

# Estas dos sentencias:

a = 10
print "El valor de a: %d" % a

# son equivalentes a:

a = 10; print "El valor de a: %d" % a

# Las sentencias típicamente generan efectos secundarios, ya sea
# generando salida a alternado el estado de algún otro objeto.

# Las expresiones simplemente se evalúan de derecha a izquierda y
# finalmente se resuelven a algún valor literal, es decir, un valor
# que ya no puede ser más trabajado.

assert 4 == (3-1) * (1 + 1)

# Ahora, algunas expresiones son sentencias, pero no todas las
# sentencias son expresiones

# La siguiente línea de código...
# type(if 3>5: print "Hola" else print "Chau")
# ...levanta un error de sintáxis

# En cambio, esta forma de condicional si se evalúa a un valor.
edad = 20
assert "Mayor de edad" if edad >= 18 else "Menor de edad"

########################################################################
## 00. TIPOS DE DATOS BÁSICOS                                         ##
########################################################################

# type nos ayuda indicandonos el tipo de dato
print type('x')
# Debe mostrar: <type 'str'>

cadena = 'abc123'
assert isinstance(cadena, str) == True
assert type(cadena).__name__ == 'str'

entero = 42
assert isinstance(entero, int) == True

largo = 2147483647 + 1
assert isinstance(largo, long) == True

flotante = 18.9311
assert isinstance(flotante, float) == True

lista = [1,1,2,3,5,8,13,21]
assert isinstance(lista, list) == True

tupla = ('L','M','X','J','V','S','D')
assert isinstance(tupla, tuple) == True

diccionario = {'nombre':'Guido', 'apellido':'van Rossum'}
assert isinstance(diccionario, dict) == True

conjunto = {'nuevo','observado','pendiente','en-progreso','hecho','cerrado'}
assert isinstance(conjunto, set) == True

objeto = object()
assert isinstance(objeto, object) == True

suma = lambda a,b: a + b
assert type(suma).__name__ == 'function'


def resta(a, b):
    return a - b
assert type(resta).__name__ == 'function'


########################################################################
## 00.00 NUMERICOS: int, long, float.                                 ##
########################################################################

assert 1 + 1 == 2
assert 10 - 1 == 9
assert 2 * 3 == 6
assert 10 / 5 == 2
assert 19 / 4.0 == 4.75
assert 19 // 4 == 4  # equivalente a math.floor(19 / 4)
assert 19 % 4 == 3 # residuo
assert abs(-5) == 5
assert 3**4 == 81 # potencia

########################################################################
## 00.00 CADENAS.                                                     ##
########################################################################

cadena = 'delimitada por comillas simples'
cadena = "delimitada por comillas dobles"
cadena = """o incluso
pueden ser
multilinea"""

# interpolación
cadena = 'resultado: --> %s <--' % 4
assert cadena == 'resultado: --> 4 <--'

# interpolación de multiples variables
cadena = 'El resultado de %s %s %s %s es: %s'
cadena_suma = cadena % ('sumar', 5, 'mas', 3, (5+3))
cadena_multip = cadena % ('multiplicar', 5, 'por', 3, (5*3))
assert cadena_suma == 'El resultado de sumar 5 mas 3 es: 8'
assert cadena_multip == 'El resultado de multiplicar 5 por 3 es: 15'

# algunas operaciones:
a = 'Python Language'
assert a.lower() == 'python language'
assert a.upper() == 'PYTHON LANGUAGE'
assert a.lower().capitalize()  == 'Python language'
assert a.strip('Pyth') == 'on Language'
assert a.strip('age') == 'Python Langu'
assert a.lstrip('Py') == 'thon Language'
assert a.split(' ') == ['Python','Language']
assert 'X'.join(a.split(' ')) == 'PythonXLanguage'
assert '-'.join(['lunes' , 'martes', 'viernes']) == 'lunes-martes-viernes'
assert 'uno' + 'dos' == 'unodos'
assert str(10) == '10'
assert 'uno' + 'dos' + str(3) == 'unodos3'
assert a.startswith('Pyth')
assert not a.startswith('PHP')
assert a.endswith('age')
otrolang = a.replace('Language', 'Lenguaje').replace('Python','Ruby')
assert otrolang == 'Ruby Lenguaje'

# iterando la cadena
for caracter in 'Una cadena':
    assert len(caracter) == 1
    assert isinstance(caracter, str) == True
    assert type(caracter).__name__ == 'str'


#exit(1)
########################################################################
## 00. VARIABLES VS CONSTANTES                                        ##
########################################################################

# ==> ERNESTO <==

########################################################################
## 00. ASIGNACIÓN VS COMPARACIÓN                                      ##
########################################################################

########################################################################
## 00. CONTADORES, ACUMULADORES Y BANDERAS                            ##
########################################################################

# Los contadores son variables que registran un cambio constante,
# es decir, cada vez que cambian de valor, el cambio es el mismo
# quantitativamente.

contador = 0

# Hacemos una venta
contador += 1

# Vendemos otro item
contador += 1

# Logramos hacer una tercera venta
contador += 1

# El cambio no tiene porque ser aritmético, ni de una unidad en
# una unidad, ni en en sentido positivo:

contador = 10000
contador -= 1000
contador -= 1000
contador -= 1000
contador -= 1000
contador -= 1000

assert contador == 5000

# Elevando 2 a base 5

valor = 2 ** 0 # 1
valor *= 2
valor *= 2
valor *= 2
valor *= 2
valor *= 2

assert valor == 32

# En cambio, un acumulador es una variable que recibe cambios que
# van variando cuantitativamente:

# Monto vendido
ventas = 0.0

# Vendemos un producto de S/. 500
ventas += 500.0

# Vendemos un producto de S/. 1200

ventas += 1200.0

# Vendemos un producto de S/. 800

ventas += 800.0

assert ventas == 2500

# Otro ejemplo clásico de acumulador es sumar las notas de un
# curso antes de sacar el promedio

notas = 0.0
num_notas = 0

# Primera nota
notas += 14.0
num_notas += 1

# Segunda nota
notas += 8.0
num_notas += 1

# Tercera nota
notas += 17.0
num_notas += 1

assert notas == 39.0
assert num_notas == 3

promedio = notas / float(num_notas)
assert promedio == 13.0

# Finalmente, una bandera es una variable que toma estados según
# estos describan el estado de otra variable del dominio del
# problema que está siendo monitoreada.

# Ejemplos:

TURNO_MANIANA = 1
TURNO_TARDE = 2
TURNO_NOCHE = 3
TURNO_MADRUGADA = 4

# Son las 6 AM
turno_actual = TURNO_MANIANA

# A las 8am se nos ocurre consultar

assert turno_actual == TURNO_MANIANA

# Son las 12 PM y hay cambio de turno
turno_actual = TURNO_TARDE

# A las 3pm se nos ocurre consultar

assert turno_actual == TURNO_TARDE

# Son las 6 PM y hay cambio de turno
turno_actual = TURNO_NOCHE

# Son las 00 AM y hay cambio de turno
turno_actual = TURNO_MADRUGADA

# A las 5am consultamos el turno actual

assert turno_actual == TURNO_MADRUGADA

########################################################################
## 00. CONDICIONALES                                                  ##
########################################################################

# ==> ERNESTO <==

########################################################################
## 00. BUCLES                                                         ##
########################################################################

# ==> ERNESTO <==

# * while
# * for

########################################################################
## 00. LISTAS                                                         ##
########################################################################

# ==> ERNESTO <==

########################################################################
## 00. DICCIONARIOS                                                   ##
########################################################################

# ==> ERNESTO <==

########################################################################
## 00. CONJUNTOS                                                   ##
########################################################################

# ==> ERNESTO <==

########################################################################
## 00. CLOSURES                                                       ##
########################################################################

# ==> ANTONIO <==

########################################################################
## 00. LAMBDAS                                                        ##
########################################################################

# ==> ERNESTO <==

# * Lambdas que sin argumentos
# * Lambdas con argumentos
# * Indicar que los lambdas solo aceptan expresiones simples
# * Función espejo como lambda

def suma(a, b):
    return a + b

suma = lambda a, b: a + b

assert (lambda a, b: a + b)(1,1) == 2

########################################################################
## 00. MAP, REDUCE y FILTER                                           ##
########################################################################

# ==> ERNESTO <==

########################################################################
## 00. LISTAS POR COMPRENSIÓN                                         ##
########################################################################

# ==> ANTONIO <==

########################################################################
## 00. CLASES Y OBJETOS                                               ##
########################################################################

########################################################################
## 00. PERSONALIZANDO EXCEPCIONES                                     ##
########################################################################



# ==> ANTONIO <==

########################################################################
## 00. PROTOCOLOS                                                     ##
########################################################################

# ==> ANTONIO <==

########################################################################
## 00. PRINCIPALES MÉTODOS MÁGICOS                                    ##
########################################################################

# ==> ERNESTO <==

########################################################################
## 00. CALLABLES                                                      ##
########################################################################

# En Python, cualquier objeto que implementa el método mágico __call__
# puede ser invocado como si se tratara de una función. Lo que en
# realidad sucede es que los argumentos son pasados a su método mágico
# __call__.

class Sumadora(object):

    def __init__(self, sumando=1):
        self.sumando = sumando

    def __call__(self, numero):
        return numero + self.sumando


sumador_de_cincos = Sumadora(sumando=5)
assert sumador_de_cincos(0) == 5
assert sumador_de_cincos(100) == 105

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

########################################################################
## 00. ITERADORES                                                     ##
########################################################################

# Los iteradores con objetos que devuelven elementos de una secuancia
# uno a la vez cuando se invoca la función next() y finalmente lanzan
# la excepción StopIteration cuando ya no quedan más elementos por
# entregar.

class IteradorVocales(object):

    VOCALES = "aeiou"

    def __init__(self):
        self.apuntador = 0

    def next(self):
        if self.apuntador < len(self.VOCALES):
            resultado = self.VOCALES[self.apuntador]
            self.apuntador += 1
            return resultado
        else:
            raise StopIteration

obj = IteradorVocales()
assert obj.next() == 'a'
assert obj.next() == 'e'
assert obj.next() == 'i'
assert obj.next() == 'o'
assert obj.next() == 'u'

try:
    obj.next()
except StopIteration:
    print u"No hay más elementos por iterar"

########################################################################
## 00. ITERABLES                                                      ##
########################################################################

# Los iterables son objetos que devuelven un iterador cuando se invoca
# a su método mágico __iter__.

# Los iteradores funcionan directamente con la estructura de control
# for, así por ejemplo:

class IteradorVocales(object):

    VOCALES = "aeiou"

    def __init__(self):
        self.apuntador = 0

    def next(self):
        if self.apuntador < len(self.VOCALES):
            resultado = self.VOCALES[self.apuntador]
            self.apuntador += 1
            return resultado
        else:
            raise StopIteration

    def __iter__(self):
        return self

for vocal in IteradorVocales():
    print vocal

# Muchas veces el iterador que devuelve el iterable es el mismo objeto
# iterador que implementa el método mágico __iter__ y que por lo tanto
# se convierte también en iterable.

# Otra forma de construir un iterador es pasando cualquier secuencia
# por la función iter().

VOCALES = 'aeiou'

for vocal in VOCALES:
    print vocal

for vocal in iter(VOCALES):
    print vocal

i = 0
iterador = iter(VOCALES)

while True:
    try:
        print iterador.next()
    except StopIteration:
        break

# Es necesario tener en cuenta que el objeto devuelto por el método
# mágico __iter__ *NO* necesariamente tiene que ser el propio objeto
# en el que se invoca el método mágico, sino que puede ser algo
# distinto, como por ejemplo, un iterador creado con el método
# __iter__  a partir de un secuencia interna.

class Aula(object):

    def __init__(self, docente):
        self.docente = docente
        self.alumnos = []

    def agregar_alumno(self, nombre_alumno):
        if nombre_alumno not in self.alumnos:
            self.alumnos.append(nombre_alumno)

    def __iter__(self):
        return iter(self.alumnos)

aula = Aula(docente='Dora Gutierrez')
aula.agregar_alumno("Juan Perez")
aula.agregar_alumno("Esperanza Ramos")
aula.agregar_alumno(u"Domingo Jiménez")

for alumno in aula:
    print alumno

########################################################################
## 00. GENERADORES                                                    ##
########################################################################

########################################################################
## 00. EXPRESIONES DE GENERADOR                                       ##
########################################################################

# Las expresiones de generador son conceptualmente idénticas a las
# listas por comprensión
