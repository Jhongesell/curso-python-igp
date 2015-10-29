#!/usr/bin/env python
# -*- coding: utf8 -*-


def parentesis(s):
    return '(%s)' % s


def corchetes(s):
    return '[%s]' % s


print parentesis('1')
print corchetes('2')


##################################
# Decorando mediante composición #
##################################
def corchetesYparentesis1(s):
    return parentesis(corchetes(s))

print corchetesYparentesis1('3')


