#!/usr/bin/python

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield 'Hello World, uwsgi is speaking'
