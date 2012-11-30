#!/usr/bin/env python27
#-*- coding:utf-8 -*-
import sae
import web, os
from setting import *
from main import *

app = web.application(urls, globals()).wsgifunc()

#app = web.application(urls,globals(), autoreload=True).wsgifunc() 

#web.config.debug = False
#curdir = os.path.dirname(__file__)

#if web.config.get('_session') is None:    
session = web.session.Session(app, web.session.DiskStore('session'), initializer = {'islogin':False, 'uid':None})
web.config._session = session
#else:
#    session = web.config._session
application = sae.create_wsgi_app(app)


if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
