#!/usr/bin/env python27
#-*- coding:utf-8 -*-
import MySQLdb,sys


conn = MySQLdb.connect(host='localhost',user='root',passwd='')
cursor = conn.cursor()
cursor.execute("create database if not exists notes")

conn.select_db('notes')
cursor.execute("create table if not exists notes(nid int(10) not null primary key auto_increment,date date,time time, text text  default null ,comment int(10) default 0)")
cursor.execute("create table if not exists user(uid int(5) not null primary key auto_increment,user varchar(10) not null,passwd varchar(50) not null ,perm int(2) default 1,datetime datetime)")
cursor.execute("create table if not exists comment(nid int(10) not null primary key auto_increment,cid int(10) not null,datetime datetime,name varchar(20)  default '匿名',mail varchar(20) default '保密', comment text )")
cursor.execute("insert into user(user, passwd) values('admin', password('123456'))")
cursor.execute("insert into notes(date,time,text)values(now(),now(),'hello world')")
cursor.close()
conn.close()


