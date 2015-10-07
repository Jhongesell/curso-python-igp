import random

a = random.randint(1,10)
print (a)

if a > 6:
  print 'mayor a 6'
elif a > 3:
  print 'mayor a 3'
else:
  print 'no es mayor a 3'

if (a <= 2) or (a >= 8):
  print 'a es menor a 2 o mayor a 8'


for (i,n) in enumerate(range(10,10+a)):
  print '-> ', i , ' : ', n


#i = i + 1 -> Syntactic Sugar, Azucar Sintactico

print '\n While:'

i = 0
while (True):
  i += 1
  print i
  if (i>7):
    break
  if (i>3):
    continue
  print 'otra linea'

print 'FINAL'
print '\nEjempl 2:'


i = 0
j = 0
while i < 3:
  while  j < 3:
    print i,j
    j += 1
    if (i==j) and i != 0:
      #exit(0)
      break
  if (i==j) and i != 0:
    break
  i += 1
  j = 0

print 'FINAL2'
