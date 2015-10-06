#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 2
b = 'Saludo'
print dir()
print locals()

print type (a)
print type (b)


print dir('hola')
print dir(1==1)
print dir(None)


print '''
+--------------------------------+
| Cadenas: delimitadas por ' o " |
+--------------------------------+
'''

a = 'Python Language'
print type(a)
print a
print a.lower()
print a.upper()
print a.lower().capitalize()
print a.strip('Pyth')
print a.strip('age')
print a.lstrip('Py')
print a.split(' ')
print 'X'.join(a.split(' '))

print '\n Ejemplo Join'
partes = ['lunes' , 'martes', 'viernes']
print partes
unasolacadena = '<--->'.join(partes)
print unasolacadena


print 'A' + ' y ' + 'B'
print '1' + ' y ' + '2'
print str(1) + ' y ' + str(2)

print a
print a.startswith('Pyth')
print a.startswith('PHP')
print a.endswith('age')

print a[7]
print a.replace('Language', 'Lenguaje').replace('Python','Ruby')

print a

for c in a:
  if c == 'a':
    print str(4)
  else:
    print c

print '''
+----------------------------+
| Listas: delimitadas por [] |
+----------------------------+
'''

l = ['Lunes' , 'Miercoles', 'Viernes']
print l

l.append('Domingo')
print l

l.insert(1,'Martes')
print l

l.extend(['Varios','Dias'])
print l

l.extend('ABC')
print l

print range(11,15)
print range(4)

print range(0,40,7)

print l

for i in range(4):
  print 'borrando: ', l[len(l)-1]
  del l[len(l)-1]

print l
l.remove('Varios')
print l


l.insert(3,'Jueves')
l.insert(5,'Sabado')
print l

dow = list(l);

l.reverse()
print l

l.sort()
print l

l.append('Ultimo')
print l

l.pop()
print l

print dow
print dow[1]
print dow[-2]

print '\n Slicing:'

print dow[2:4]
print dow[5:]
print dow[:3]
print dow[::3]
print dow[::2]
print dow[1::2]

(a,b) = dow[1],dow[5]
print a
print b

print '''
+----------------------------+
| Tuplas: delimitadas por () |
+----------------------------+
'''

t = tuple(dow)
print t
print type (t)

print (1,2,3)
print (1,2)
print (1)

print type( (1,2,3) )
print type( (1,2)   )
print type( (1)     )
print type( (1,)     )


print '''
+-----------------------------------------+
| Diccionario o Mapas: delimitados por {} |
+-----------------------------------------+
'''

d = {}
print type (d)

d = {'user':'Ernesto', 'age': 29, 'Langs':['php','js','python']}
print d

del d['Langs']
print d

d['apellido'] = 'Anaya'
print d

print d.values()
print d.keys()
print d.items()

print '\n Iterando keys: '
for i in d:
  print i

print '\n Iterando values: '
for i in d:
  print d[i]

print '\n Iterando keys y values: '
for (k, v) in d.items():
  print str(k) + ' => ' + str(v)


print '\n Iterando keys y values eficientemente: '
for (k, v) in d.iteritems():
  print str(k) + ' => ' + str(v)



# in
print '\n --- Operador in: '
print ( 1 in [1,2,3] )
print ( 4 in [1,2,3] )
print ( 1 in (1,2,3) )
print ( 4 in (1,2,3) )
print ( 1 in {1:'A',2:'B',3:'C'} )
print ( 4 in {1:'A',2:'B',3:'C'} )


print '''

Conjuntos o Sets:
=========================
'''

#s = {1, 2, 3}
#print type(s)


s1 = set(range(1,5))
s2 = set(range(3,9))

print s1

s2.add(13)
s2.add(13)
s2.add(13)
print s2

print type ( s1 )

print '\n Union: s1 | s2'
print (s1 | s2)

print '\n Diferencia: s1 - s2'
print (s1 - s2)

print '\n Intersección: s1 & s2'
print (s1 & s2)

print '\n Union - Intersección: s1 ^ s2'
print (s1 ^ s2)



print '\n ------ Cast'
a = (1,2,3,'4','a')

print str(a).upper()
print list(a)
