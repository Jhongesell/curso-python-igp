#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import random

if len(sys.argv)!=3:
    msg = 'Uso: ' + sys.argv[0] + ' n AM|FM\n'
    exit(msg)


def random_stations(n, tipo):
    radio = {
        'AM': {
            'band_min': 540,
            'band_max': 1600,
            'unit': 'kHz',
            'n' : 106
        },
        'FM': {
            'band_min': 88.1,
            'band_max': 108.1,
            'unit': 'MHz',
            'n' : 100
        },
    }
    config = radio[tipo]
    step = (config['band_max'] - config['band_min']) / config['n']
    stations = []
    for i in range(n):
        r = random.randint(1,config['n'])
        stations.append(str(config['band_min'] + step * r)+config['unit'])
    print '  '.join(stations)

random_stations(int(sys.argv[1]), sys.argv[2].upper())