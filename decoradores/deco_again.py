# -*- coding: utf8 -*-

def parentesis(s):
    return '(%s)' % s;

# un decorador es una funcion que recibe una funcion y devuelve una funcion

def entendi(funcion_a_decorar):
    def aux(s):
        #return funcion_a_decorar(parentesis(s))
        return funcion_a_decorar(funcion_a_decorar(funcion_a_decorar(s)))
    return aux


@entendi
@entendi
@entendi
def corchetes(s):
    return '[%s]' % s

#corchetes = entendi(corchetes)


print corchetes('python3')
# [python]
# ([python])
# [(python)]
# (((python)))  <---

