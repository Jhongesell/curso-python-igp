#!/usr/bin/env python
# -*- coding: utf8 -*-

l1 = range(1, 10 + 1) 

l2 = [n % 2 == 0 for n in range(1, 10 + 1)]

sumar = lambda a, b: a + b
logic_and = lambda a, b: a and b
logic_or = lambda a, b: a or b

resultado1 = reduce(sumar, l1, 0)
resultado2 = reduce(logic_and, l2, True)
resultado3 = reduce(logic_or, l2, True)

print resultado1
print resultado2
print resultado3
