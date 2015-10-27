#!/usr/bin/env python
# -*- coding: utf8 -*-

# convierte un archivo csv a una lista
def csv2list(file):
    return [row.strip().split(',') for row in open(file).readlines()]

# genera cadena para imprimir titulo de la pelicula
def pelicula2string(texto):
    lado = '*' * (len(texto)+4)
    return '%s\n* %s *\n%s' % (lado,texto,lado)

# genera cadena para imprimir cine
def cine2string(texto):
    return '\n   %s:\n' % texto.upper()

# genera cadena para imprimir sala
def sala2string(sala, horarios):
    return '      - Sala %s:  %s' % (sala, '  '.join(horarios))


cines = dict(csv2list('cines.csv'))
peliculas = dict(csv2list('peliculas.csv'))
funciones = csv2list('funciones.csv')

cartelera = {}

for cid, pid, sala, horario in funciones:

    # Peliculas
    if not cartelera.has_key(pid):
        cartelera[pid] = {}
    cartelera[pid]['titulo'] = peliculas[pid]
    if not cartelera[pid].has_key('cines'):
        cartelera[pid]['cines'] = {}

    # Cines
    if not cartelera[pid]['cines'].has_key(cid):
        cartelera[pid]['cines'][cid] = {}
    cartelera[pid]['cines'][cid]['nombre'] = cines[cid]
    if not cartelera[pid]['cines'][cid].has_key('salas'):
        cartelera[pid]['cines'][cid]['salas'] = {}

    #salas
    if not cartelera[pid]['cines'][cid]['salas'].has_key(sala):
        cartelera[pid]['cines'][cid]['salas'][sala] = []
    cartelera[pid]['cines'][cid]['salas'][sala].append(horario)

# Imprimiendo la data
for pid, pelicula in cartelera.items():
    print pelicula2string(pelicula['titulo'])
    for cid, cine in pelicula['cines'].items():
        print cine2string(cine['nombre'])
        for sala,horarios in cine['salas'].items():
            print sala2string(sala, horarios)
    print '\n\n'
