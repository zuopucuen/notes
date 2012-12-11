#!/usr/bin/env python27
#-*- coding:utf-8 -*-
import fenye
from setting import *

def make_html(s):
    return web.websafe(s).replace('\r\n', '<br />')
web.template.Template.globals['make_html'] = make_html

def getuserid():
    if web.config._session.get('uid') is None:
        return False
    else:
        return web.config._session.uid

class reindex:
    def GET(self):
        raise web.seeother('/')

class index:
    def GET(self):
        uid = getuserid()
        result = []
        i = web.input()
        ye = 1
        yeshu = None

        if 'page' in i:
            ye = int(i.page)

        if 'date' in i:
            data = db.query('''select * from notes where date="%s"''' % i.date)
            if data:
                result.append([i.date,data])
                return render.main(result,"index",uid,[None])
            else:
                return render.error("sorry，该页数不存在！")
        else:
            #dates = db.query("select distinct date from notes order by date  desc")

            r = db.query('''select count(distinct date) as nu from notes''')
            yeshu = fenye.getyeshu(r[0].nu)
            minmax  = fenye.getminmax(ye)

            dates = db.query('''select distinct date from notes order by date desc limit %s,%s''' % (minmax[0],minmax[1]))
            for date in dates:
                datas = db.query('''select * from notes where date="%s" order by time desc''' % date.date)
                result.append([date.date,datas])
        return render.main(result,"index",uid,[yeshu,ye,"/?page="])
class new:
    def GET(self):
        raise web.seeother("/")

class about:
    def GET(self):
        uid = getuserid()
        return render.main('','about',uid,[None])
class login:
    def GET(self):
        return render.login()
    
    def POST(self):
        a = web.input()
        b = db.query('''select uid,user,passwd from user where user="%s" and passwd=password("%s")''' % (a.username,a.password))
        if b:
            uid = b[0].uid
            session = web.config._session
            session.islogin = True
            session.uid = uid
            #web.setcookie('uid', uid, 360000)
            return web.seeother("/")
        else:
            return render.error("用户名或密码不正确！")
class logout:
    def GET(self):
        web.config._session.kill()
        raise web.seeother("/")
class add:
    def GET(self):
        uid = getuserid()
        if uid:
            return render.main("","add",uid,[None])
        else:
            return render.error("请登录")

    def POST(self):
        uid = getuserid()
        if uid:
            i = web.input()
            db.query('''insert into notes(date,time,text)values(now(),now(),'%s')'''% i.post_content )
            web.seeother("/")
        else:
            return render.error("请登录")
class alter:
    def GET(self):
        uid = getuserid()
        if uid:
            i = web.input()
            result = db.query('''select nid,text from notes where nid="%s"''' % i.id)
            return render.main(result,"alter",uid,[None])
        else: 
            return render.error("请登录")
    def POST(self):
        uid = getuserid()
        if uid:
            i = web.input()
            db.query('''update notes set text="%s" where id="%s"''' % (i.post_content,i.id))
            raise web.seeother("/")
        else:
            return render.error("请登录")
class search:
    def GET(self):
        uid = getuserid()
        result = []
        i = web.input()
        ye = 1

        if "page" in i:
            ye = int(i.page)

        if "search" in i:
            if  "'" in i.search:
                return render.error('''请不要在关键字起中包含“ ''”''')
            r  = db.query('''select count(nid) as nu from notes where text like '%s%s%s' order by date desc''' %("%",i.search,"%"))[0].nu 
            if r != 0:
                yeshu = fenye.getyeshu(r)
                minmax = fenye.getminmax(ye)
                datas = db.query('''select * from notes where text like '%s%s%s' order by date desc limit %s,%s''' %("%",i.search,"%",minmax[0],minmax[1]))

                for j in datas:
                    result.append([j.date,[j]])
                return render.main(result,"index",uid,[yeshu,ye,"/search?search=%s&page=" % i.search])
            else:
                return render.error("sorry，没有找到内容！")
        else:
            raise web.seeother("/")
class comment:
    def GET(self):
        uid = getuserid()
        result = []
        i = web.input()
        
        if 'id' in i:
            nid = i.id
            print nid
            data = db.query('''select * from notes where nid='%s' ''' % nid)[0]
            r = db.query('''select * from comment where nid='%s' ''' % nid)
            result.append([data.date,[data]])
            return render.main(result,"comment",uid,[None,r])
        else:
            raise web.seeother("/")

    def POST(self):
        i = web.input()
        c_num = db.query('''select comment from notes where nid='%s' ''' % i.id)
        if c_num:
            c_num = c_num[0].comment + 1
            n = db.query('''insert into comment(nid,datetime,name,mail,comment)values('%s',now(),'%s','%s','%s')''' % (i.id,i.name,i.mail,i.comment))
            if n:
                db.query('''update notes set comment='%s' where nid='%s' ''' % (c_num,i.id))
                return render.message("评论成功","/comment?id=%s" % i.id)
        else:
            return render.error("评论失败")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
