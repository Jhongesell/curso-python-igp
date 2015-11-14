#!/usr/bin/env python
# -*- coding: utf8 -*-

import datetime

BODY_TEMPLATE = """<html>
<head>
  <title>La hora actual en CGI</title>
</head>
<body>
   <h1>Hora</h1>
   <p>La hora es: %s</p>
   <p>Ud. tiene la IP: %s</p>
</body>
</html>
""".strip()

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = BODY_TEMPLATE % (
        str(datetime.datetime.now()),
        environ['REMOTE_ADDR']
    )
    for line in body.split('\n'):
        yield "%s\n" % line
