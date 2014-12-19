# -*- coding: UTF-8 -*-
import sys
import os
import re
from collections import Counter
import smtplib  
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
#mailto_list='xxxxxx.com'
mailto_list="xxxxxx.com" 
mail_host="smtp.xxx.com"  #设置服务器
mail_user="xxxxxxxxx"    #用户名
mail_pass="xxxxxxxxx"   #口令 
mail_postfix="xxxxxxxx.com"  #发件箱的后缀
result = None
list2 = None  
def send_mail(to_list,sub,content):
    #处理文档
    updatetype = open('xxxxxxxx.txt','r')
    line = updatetype.read()
    lines = line.split('\n')
    del lines[-1]
    list1 = Counter(lines)
    filetest = open("xxxxxxxx.txt",'a+')
    n = len(list1)
    result = [a[0]+ ' ' + str(a[1]) + '\n' for a in list1.most_common(n)]
    filetest.writelines(result)
    #发出邮件
    msg1 = MIMEMultipart()  
    me="<"+mail_user+"@"+mail_postfix+">"  
    att1 = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg1.attach(att1)
    att2 = MIMEText(open('xxxxxxxx.txt', 'rb').read(), 'base64', 'gb2312')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="xxxxxxx.txt"'
    msg1.attach(att2)
    msg1['Subject'] = sub  
    msg1['From'] = me  
    msg1['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)
        print to_list  
        server.sendmail(me, to_list, msg1.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
if __name__ == '__main__':
    filename = open('xxxxxx.txt','r')
    line = filename.read()
    lines = line.split('\n')
    del lines[-1]
    list3 = Counter(lines)
    m = len(list3)
    result1 = [a[0]+ ' 'for a in list3.most_common(m)]
    filetest2 = open('xxxxxx.txt','a+')
    filetest2.writelines(result1)
    filetest2.close()
    filetest2 = open('xxxxx.txt','r')
    line1 = filetest2.read()
    mailto_list = str(mailto_list)
    print mailto_list 
    if send_mail(mailto_list,"xxxxx Report","This is report about xxxx update,%s" % line1):  
        print "Success"  
    else:  
        print "Failure"