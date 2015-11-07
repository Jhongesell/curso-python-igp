#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys

print "Antes de activar el entorno virtual:"
print sys.path

activate_this = '/code/cursos/curso-python-igp/paquetes/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

print u"Después de activar el entorno virtual:"
print sys.path
