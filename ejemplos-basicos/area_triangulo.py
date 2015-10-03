#!/usr/bin/env python
# -*- coding: utf8 -*-

titulo = "Area del triángulo"

print titulo
print '=' * len(titulo)

print 
base = float(raw_input("Ingrese la base: "))
altura = float(raw_input("Ingrese la altura: "))

area = base * altura / 2.0

print "Area: %.2f" % area