#!/usr/bin/env python27
#-*- coding:utf-8 -*-
import MySQLdb,sys


conn = MySQLdb.connect(host='localhost',user='root',passwd='')
cursor = conn.cursor()
cursor.execute("create database if not exists notes")

conn.select_db('notes')
cursor.execute("create table if not exists notes(id int(10) not null primary key auto_increment,date date,time time, text text  default null ,comment int(10));")
cursor.execute("create table if not exists user(uid int(5) not null primary key auto_increment,user varchar(10) not null,passwd varchar(10) not null ,perm int(2) default 1,datetime datetime)")
cursor.execute("create table if not exists comment(id int(10) not null primary key auto_increment,cid int(10) not null,datetime datetime,name varchar(20)  default '匿名',mail varchar(20) default '保密', comment text );")
cursor.close()
conn.close()


