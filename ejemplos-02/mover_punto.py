#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import random
import time

ANCHO = 20
ALTO = 20

DORMIR_EN_SEGUNDOS = 0.20

POSICION_INICIAL = {'x': 10, 'y': 10}

def limpiar_pantalla():
    os.system('clear')

def movimiento_aleatorio():
    return random.randint(-1, 1)

def detectar_colision(posicion):
    return posicion['x'] == 0 or posicion['x'] == ANCHO \
        or posicion['y'] == 0 or posicion['y'] == ALTO

def desplazar(posicion, mov_x, mov_y):
    return {
        'x': posicion['x'] + mov_x,
        'y': posicion['y'] + mov_y
    }

def posicion_valida(posicion):
    return posicion['x'] in range(0, ANCHO + 1) and \
        posicion['y'] in range(0, ALTO + 1)

def imprimir_posicion(posicion):
    print "x: %d y: %d" % (posicion['x'], posicion['y'])

def imprimir_direccion(mov_x, mov_y):
    print "mov_x: %d mov_y: %d" % (mov_x, mov_y)

def imprimir_cursor(posicion):
    elementos = []
    elementos.append('\n' * posicion['y'])
    elementos.append(' ' * (posicion['x'] - 1))
    elementos.append('*')
    print ''.join(elementos)


mov_x = 0
mov_y = 0

if __name__ == '__main__':

    limpiar_pantalla()

    while mov_x == 0 and mov_y == 0:
        mov_x = movimiento_aleatorio()
        mov_y = movimiento_aleatorio()

    posicion = POSICION_INICIAL

    while True:
        imprimir_posicion(posicion)
        imprimir_direccion(mov_x, mov_y)
        imprimir_cursor(posicion)
        time.sleep(DORMIR_EN_SEGUNDOS)
        limpiar_pantalla()
        if detectar_colision(posicion):
            encontrado = False
            while not encontrado:
                mov_x = movimiento_aleatorio()
                mov_y = movimiento_aleatorio()
                posicion_prueba = \
                    desplazar(posicion, mov_x, mov_y)
                if posicion_valida(posicion_prueba):
                    encontrado = True
        posicion = desplazar(posicion, mov_x, mov_y)
