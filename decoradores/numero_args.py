# -*- coding: utf8 -*-
# hacer un decorador que
# Si el # de args x posición de la funcion decorada entonces devuelve un
# valor por defecto


def deco(default):
    def decorador(funcion_a_decorar):
        def aux(*args, **kwargs):
            if len(args) % 2 ==0:
                return default
            else:
                return funcion_a_decorar(*args, **kwargs)
        return aux
    return decorador

@deco(2000)
def nuevosum(*args):
    return sum(args)

#print nuevosum(1,2,3,4)
#sum = deco(20)(sum)

print nuevosum(1) # 1
print nuevosum(1,2) # 20
print nuevosum(1,2,3) # 6
print nuevosum(1,2,3,4) # 20
print nuevosum(1,2,3,4, 5) # 15
