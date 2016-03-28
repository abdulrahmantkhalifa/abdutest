#! /usr/bin/env python

from wsgiref.simple_server import make_server

def application(environ, start_response):


    # Adding strings to the response body
    response_body = ['<img src="Atlantis Nebula UHD.jpg">']

    # So the content-lenght is the sum of all string's lengths

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
    ]

    start_response(status, response_headers)
    return response_body

httpd = make_server('localhost', 8051, application)
httpd.handle_request()