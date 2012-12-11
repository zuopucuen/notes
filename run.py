#!/usr/bin/env python27
#-*- coding:utf-8 -*-
import web, os
from setting import *
from main import *

app = web.application(urls, globals())

#web.config.debug = False
curdir = os.path.dirname(__file__)

if web.config.get('_session') is None:    
    session = web.session.Session(app, web.session.DiskStore('session'), initializer = {'islogin':False, 'uid':None})
    web.config._session = session
else:
    session = web.config._session

if __name__ == "__main__":
    app.run()
