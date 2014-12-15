#!/usr/bin/python
# -*- coding:utf8 -*-
import os
import psycopg2
def readinsert():
    con = psycopg2.connect(host='192.168.20.20', port=5432, database ='vulnerability3', user='postgres')
    cur = con.cursor()
    filename = open('name.txt','r')
    lines = filename.readlines()
    i = 407 
    for  line in lines:
        i = i + 1
        strname = '未完成'
        sql = '''UPDATE production.expinfo SET name = '%s' where id_key = '%s' ''' % (line,i)
        #sql = '''INSERT INTO production.expinfo(status)VALUES ('%s'); ''' % (strname)
        cur.execute(sql)
        con.commit()
readinsert()