import MySQLdb
import urllib2
import datetime

db = MySQLdb.connect(host="10.211.55.30",    # your host, usually localhost
                     user="root",         # your username
                     passwd="bigmaster",  # your password
                     db="checklink",      # name of the data base
                     port=3308)        # port if tge data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM m3u8linkcheck")

# m3u8 = open('m3u8.txt','r')
# for bR in m3u8:
#     print bR


# print all the first cell of all the rows
# for row in cur.fetchall():
#     checkt = row[0]
#     url = row[1]
#     status = row[2]
#     print checkt,url,status


#Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO m3u8linkcheck VALUES (%s,%s,%s)""",('2016-02-24 17:55:49','http://www.teenee.com','1')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()


#    >>> #insert to table
# ... try:
# ...     cursor.execute("""INSERT INTO anooog1 VALUES (%s,%s)""",(188,90))
# ...     db.commit()
# ... except:
# ...     db.rollback()



db.close()
