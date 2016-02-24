DATABASE_HOST = "10.211.55.30"
DATABASE_USER = "root"
DATABASE_NAME = "checklink"
DATABASE_PASSWD = "bigmaster"
DATABASE_PORT = 3306

import MySQLdb

# Connect to the Database
db=MySQLdb.connect(host=DATABASE_HOST,user=DATABASE_USER,
 passwd=DATABASE_PASSWD, port=int(DATABASE_PORT))

# Make the database cursor
cursor = db.cursor()

# Drop and create the database
cursor.execute("drop database %s; create database %s;" % (DATABASE_NAME, DATABASE_NAME))

# Re connect to database using db=DATABASE_NAME
db=MySQLdb.connect(host=DATABASE_HOST,user=DATABASE_USER,
 passwd=DATABASE_PASSWD, db=DATABASE_NAME, port=int(DATABASE_PORT))
cursor = db.cursor()

# Create the table for the wave data
from math import sin, cos, tan
cursor.execute("""CREATE TABLE waves (
id INT NOT NULL AUTO_INCREMENT,
PRIMARY KEY(id),
sin FLOAT,
cos FLOAT,
tan FLOAT,
date INT);
""")

# Insert the sine wave data
from datetime import datetime

def STAMP( dt ):
  """ turns a python datetime object into a unix time stamp (seconds) """
  import time
  return int(time.mktime( dt.timetuple() ))

now = STAMP( datetime.now() )
five_mins = 60*5

sql = "INSERT INTO waves (sin, cos, tan, date) VALUES (%s, %s, %s, %s);"

# Insert the data into the table
for i in range(1000):
  s = now - i*five_mins
  cursor.execute(sql % ( sin(s), cos(s), tan(s), s ))
  print s
