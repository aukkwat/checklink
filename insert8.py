import MySQLdb
import time
import datetime

today = time.strftime("%Y-%m-%d")
datepass = ('{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))


db = MySQLdb.connect("docker", "root", "bigmaster", "checklink", 3306)
timestamp = ('{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
bR = 'http://www.google.co.th'

passstatus = 1
errorstatus = 0
nonestatus = -1

with db:
    cursor = db.cursor()
    sql = '''INSERT INTO linkchecked(datecheck, urlcheck, statuscheck) \
                    VALUES (%s, %s, %s)'''
    cursor.execute(sql, (timestamp, bR, passstatus))
