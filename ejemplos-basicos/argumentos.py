#!/usr/bin/env python
# -*- coding: utf8 *-*

import sys

if len(sys.argv) != 4:
    print "Uso: %s <argumento 1> <argumento 2> <argumento 3>" % \
        sys.argv[0]
    sys.exit(1)

print sys.argv[:4]
