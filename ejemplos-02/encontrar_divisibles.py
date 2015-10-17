#!/usr/bin/env python
# -*- coding: utf8 -*-

NUM_DIVISIBLES = 10
DIVISOR = 3
INICIO = 101

if __name__ == '__main__':
    encontrados = 0
    candidato = INICIO
    while encontrados < NUM_DIVISIBLES:
        if candidato % DIVISOR == 0:
            encontrados += 1
            print candidato
        candidato += 1
