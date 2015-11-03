#!/usr/bin/env python;
# -*- coding: utf8 -*-;

def parentesis(s):
    return '(%s)' % s;


def corchetes(s):
    return '[%s]' % s


print parentesis('1');
print corchetes('2');


##################################
# Decorando mediante composición #
##################################
def corchetesYparentesis1(s):
    return parentesis(corchetes(s))

print corchetesYparentesis1('3')


##########################
# Decorando con arroba @ #
##########################
def decoparentesis(funcCorchetes):
    def aux(s):
        print '--> b'
        salida = funcCorchetes(s)
        return parentesis(salida)
    return aux



@decoparentesis
def corchetesYparentesis2(s):
    print '--> a'
    return corchetes(s)

#corchetesYparentesis2 = decoparentesis(corchetesYparentesis2)


print corchetesYparentesis2('4')
