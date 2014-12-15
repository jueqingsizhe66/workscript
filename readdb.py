#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import psycopg2
def readinsert():
    con = psycopg2.connect(host='192.168.20.20', port=5432, database ='vulnerability3', user='postgres')
    cur = con.cursor()
    n = 0
    for  dirnames in os.listdir(r'C:/Users/admin/Desktop/test1'):
        #n = n + 1
        #sql = '''SELECT exploitname  FROM production.exploitpackage;'''
        sql = '''INSERT INTO production.exploitpackage(status, exploitname, sid, checkname)VALUES ('无法处理','%s','','yl_l'); ''' % (dirnames)
        cur.execute(sql)
        #list1 = cur.fetchall()
        con.commit()
readinsert()