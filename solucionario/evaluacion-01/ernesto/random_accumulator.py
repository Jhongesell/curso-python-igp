#!/usr/bin/env python
# -*- coding: utf8 -*-

from random import randint

lista = []

while sum(lista) <= 10000:
    lista_anterior = list(lista)
    lista.append(randint(1,100))

print lista_anterior