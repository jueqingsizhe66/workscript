# -*- coding: UTF-8 -*-
import sys
import os
import re
from collections import Counter
import smtplib  
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
#mailto_list='yongcheng_zhang@netentsec.com'
mailto_list="yule_li@netentsec.com" 
mail_host="smtp.163.com"  #设置服务器
mail_user="likujyht2"    #用户名
mail_pass="brick713isme"   #口令 
mail_postfix="163.com"  #发件箱的后缀
result = None
list2 = None  
def send_mail(to_list,sub,content):
    #处理文档
    updatetype = open('Updatetype.txt','r')
    line = updatetype.read()
    lines = line.split('\n')
    del lines[-1]
    list1 = Counter(lines)
    filetest = open("Updatetype1.txt",'a+')
    n = len(list1)
    result = [a[0]+ ' ' + str(a[1]) + '\n' for a in list1.most_common(n)]
    filetest.writelines(result)
    #发出邮件
    msg1 = MIMEMultipart()  
    me="<"+mail_user+"@"+mail_postfix+">"  
    att1 = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg1.attach(att1)
    att2 = MIMEText(open('Updatetype1.txt', 'rb').read(), 'base64', 'gb2312')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="Updatetype1.txt"'
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
    filename = open('Updateinfo.txt','r')
    line = filename.read()
    lines = line.split('\n')
    del lines[-1]
    list3 = Counter(lines)
    m = len(list3)
    result1 = [a[0]+ ' 'for a in list3.most_common(m)]
    filetest2 = open('Updateinfo1.txt','a+')
    filetest2.writelines(result1)
    filetest2.close()
    filetest2 = open('Updateinfo1.txt','r')
    line1 = filetest2.read()
    mailto_list = str(mailto_list)
    print mailto_list 
    if send_mail(mailto_list,"Snort Report","This is report about Snort update,%s" % line1):  
        print "发送成功"  
    else:  
        print "发送失败"