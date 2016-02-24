#!/usr/bin/python
#Checklink from URL
import urllib2
import datetime
import MySQLdb
### Connect Mysql Database ###
db = MySQLdb.connect("docker", "root", "bigmaster", "checklink", 3306)
### List URL Per Line in 1 URL ###
listurl = 'http://devtab.com/services/thaitv_live/'
### Database Cursor ###
cursor = db.cursor()
sql = '''INSERT INTO linkchecked(datecheck, urlcheck, statuscheck) \
                VALUES (%s, %s, %s)'''
### StatusCheck Code ###
passstatus = 1
errorstatus = 0
nonestatus = -1
### Open urllist from link and write in m3u8.txt ###
for link in urllib2.urlopen(listurl):
    link = link.replace('<br/>','\n')
    result=open("m3u8.txt","w")
    result.write(link)
### Check Url from m3u8.txt and write in DB and Text file###
m3u8 = open('m3u8.txt','r')
i = 0
j = 0
timestamp = ('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
for bR in m3u8:
    print "-"*50
    j=j+1
    datepass = ('{:%Y-%b-%d %H:%M:%S} >>>Pass>>> '.format(datetime.datetime.now()))
    dateerror = ('{:%Y-%b-%d %H:%M:%S} >>>Error>>> '.format(datetime.datetime.now()))
    try:
        if "http://" or "https://" in bR:
            br=bR
        else:
            br="http://"+bR
        BroTher = urllib2.Request(br, headers={'User-Agent' : "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT"})
        if urllib2.urlopen(BroTher).getcode() == 200 :
            i=i+1
            print "%d/%d|Ok| %s"%(i,j,br)
            result=open("normallink.txt","a")
            result.write(datepass+br)
            with db:
                cursor = db.cursor()
                cursor.execute(sql, (timestamp, bR, passstatus))
        else:
            print "%d/%d|No| %s"%(i,j,br)
            with db:
                cursor = db.cursor()
                cursor.execute(sql, (timestamp, bR, nonestatus))
    except:
        print "%d/%d|Error| %s"%(i,j,br)
        result=open("errorlink.txt","a")
        result.write(dateerror+br)
        with db:
            cursor = db.cursor()
            cursor.execute(sql, (timestamp, bR, errorstatus))
