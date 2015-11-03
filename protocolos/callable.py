def f():
    pass

f()

class Matricula():

    def __init__(self, colegio):
        print 'llamando a __init__'
        self.colegio = colegio

    def __call__(self):
        print 'llamando a __call__'
        return 'matriculando en el colegio %s' % self.colegio

unaMatricula = Matricula('Papa Francisco')

print unaMatricula()


class Sumadora(object):

    def __init__(self, sumando):
        self.sumando = sumando

    def __call__(self, x):
        return x + self.sumando

s1 = Sumadora(100)
print s1(14)


class ValidadorRuc(object):

    def __call__(self, ruc):
        self.ruc = ruc
        return self.validarTipo() and self.validarLongitud() \
    and self.validarPrefijo() and self.validarAritmetica()



    def validarTipo(self):
        return True

    def validarLongitud(self):
        return True

    def validarPrefijo(self):
        return True

    def validarAritmetica(self):
        return True


validar_ruc = ValidadorRuc()
if validar_ruc(20123456789):
    print 'RUC valido'