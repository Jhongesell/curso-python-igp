"""
WSGI config for demo1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

activate_this = '/code/cursos/curso-python-igp/django/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(1, '/code/cursos/curso-python-igp/django/demo1/')

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo1.settings")
application = get_wsgi_application()
