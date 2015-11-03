class Estado(object):
    nombre = ''

    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return '[E]Estado:%s' % self.nombre


class Ticket(object):

    estadosValidos = ['nuevo','observado','en-progreso','cerrado']

    def __init__(self, estado):
        self.estado = estado


    def __str__(self):
        return '[T:%s]' % self.estado

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):

        if type (estado).__name__ == 'str':
            estado = Estado(estado)

        if estado.nombre not in self.estadosValidos:
            estado = Estado('nuevo')
            print '!!!'

        self.__estado = estado

    estado = property(getEstado, setEstado)

    """
    # getEstado
    @property
    def estado(self):
        return self.__estado

    # setEstado
    @estado.setter
    def estado(self, estado):
        self.__estado = estado
    """



t1 = Ticket(Estado('cerrado'))
print t1
t1 = Ticket(Estado('observado'))
print t1
t1 = Ticket(Estado('noexiste'))
print t1


t1 = Ticket('en-progreso')
print t1
t1.estado = 'incorrecto'
print t1


print '=============='

class P(object):

    def __init__(self, n):
        self.n = n

    def getN(self):
        return self.__n

    def setN(self, n):
        if n<0:
            n = 0
        if n>20:
            n = 20
        self.__n = n

    n = property(getN, setN)

obj1 = P(5)
print obj1.n
obj1.n = 10
print obj1.n
obj1.n = 23
print obj1.n
obj1.n = -4
print obj1.n
