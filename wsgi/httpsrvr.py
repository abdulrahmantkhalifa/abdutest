#! /usr/bin/env python

from wsgiref.simple_server import make_server

def picture(environ, start_response):
    
    # import ipdb;ipdb.set_trace();
    # f= open("environ.txt", "w")
    # f.write(str(environ))
    # f.close()
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'), 
        # ('Content-Disposition: attachment', 'filename="Atlantis Nebula UHD.jpg"')
    ]
    start_response(status, response_headers)

    return ['<img src="Atlantis Nebula UHD.jpg">']
def home(environ, start_response):
    
    pass
def lock(environ, start_response):
    
    pass 
    # import ipdb;ipdb.set_trace(

def restful(environ, start_response):
    # import ipdb;ipdb.set_trace(
    if environ['PATH_INFO'] == '/home':
        return home
    if environ['PATH_INFO'] == '/picture':
        return picture
    if environ['PATH_INFO'] == '/lock':
        return lock

httpd = make_server("localhost", 30000, restful)
httpd.serve_forever()
