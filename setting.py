#!/usr/bin/env python27
#-*- coding:utf-8 -*-
import web
import sae.const

urls = ('', 'reindex', 
        '/','index',
        '/add','add',
        '/login','login',
        '/about','about',
        '/logout','logout',
        '/alter','alter',
        '/new', 'new',
        '/search','search',
        '/comment','comment'
        )
render = web.template.render("templates/")

db = web.database(dbn='mysql', db = sae.const.MYSQL_DB, host = sae.const.MYSQL_HOST, port = int(sae.const.MYSQL_PORT), user = sae.const.MYSQL_USER, pw = sae.const.MYSQL_PASS)
