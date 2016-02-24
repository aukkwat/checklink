import MySQLdb
import time
import datetime

today = time.strftime("%Y-%m-%d")
datepass = ('{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))


db = MySQLdb.connect("docker", "root", "bigmaster", "checklink", 3306)

with db:
    cursor = db.cursor()
    sql = '''INSERT INTO ASN(AS_NUM, AS_NAME, QUERIED, CHANGED) \
                    VALUES (%s, %s, %s, %s)'''
    cursor.execute(sql, (1, 'Level 3 Communications, Inc.', 0, datepass))
