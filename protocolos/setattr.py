# -*- coding: utf8 -*-


# Creamos una clase vacía
class A:
    pass

# instaciamos un objeto
a = A()

# podemos crearle explícitamente un atributo con punto
a.m = 'hola'

# o podemos crearle programaticamente un atributo con 'setattr()'
setattr(a, 'n', 'mundo')

# comprobemos que en ambos casos funciona
print '\nAtributos del objeto "a"'
print 'a.m = ' + a.m
print 'a.m = ' + a.n

# Ahora creamos atributos con nombre programaticamente definidos usando 'setattr()'
for i in range(10):
    nombre_atributo = 'atributo' + str(i)
    setattr(a, nombre_atributo, i*3)


# Comprobamos
print '\nOtros atributos del objeto "a"'
for attr in dir(a):
    if attr.startswith('atributo'):
        print "a.%s = %s" % (attr, getattr(a,attr))


#
# Hasta acá el uso de setattr, ahora veamos el uso de __setattr__
#

# Creamos una clase de ejemplo
class D:
    # sobre-escribimos el método __setattr__(self, key, value)
    # este método se va a ejecutar cada vez que un atributo de un
    # objeto de esta clase va a ser escrito (creado o cambiado)
    def __setattr__(self, key, value):
        # Si el valor del atributo es par, aumentarlo en 1000
        if value%2==0:
            value += 1000
        self.__dict__[key] = value


d = D()
# creamos programaticamente 10 atributos
for i in range(10):
    nombre_atributo = 'atributo' + str(i)
    setattr(d, nombre_atributo, i)

# Comprobamos: Imprimimos programaticamente el valor de esos atributos
print '\nAtributos del objeto "d"'
for attr in dir(d):
    if attr.startswith('atributo'):
        print "d.%s = %s" % (attr, getattr(d,attr))

