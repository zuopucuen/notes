#!/usr/bin/env python27
#-*- coding:utf-8 -*-
import sae
import web, os
from setting import *
from main import *
from memstore import MemStore

app = web.application(urls, globals(), autoreload = True)
app_root = os.path.dirname(__file__)
session = web.session.Session(app, MemStore(), initializer = {'islogin':False, 'uid':None})
web.config._session = session
web.config.session_parameters['timeout'] = 3600
web.config.session_parameters['ignore_expiry'] = False
application = sae.create_wsgi_app(app.wsgifunc())
