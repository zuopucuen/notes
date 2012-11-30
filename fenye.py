#!/usr/bin/env python27
#-*- coding:utf-8 -*-
import web
from setting import *

def getyeshu(r):
    num = r
    a = num / 7
    if num%7 == 0:
        return a
    else:
        return a+1
    
def getminmax(ye):
    min = (ye - 1) * 7
    max = ye * 7
    return (min,max)
