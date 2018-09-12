#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server


def application(environ, strat_response):
    strat_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello,%s!</h1>' % (environ['REMOTE_ADDR'] or 'web')
    print(environ)
    return [body.encode('utf-8')]


httpd = make_server('', 7001, application)
print('Serving HTTP on port 7000...')
httpd.serve_forever()
