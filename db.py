import MySQLdb
#connect to db
db = MySQLdb.connect(host = '10.211.55.30',user = 'root',passwd = 'bigmaster',db = 'checklink',port = 3308)

#setup cursor
cursor = db.cursor()

#create anooog1 table
cursor.execute("DROP TABLE IF EXISTS m3u8linkcheck")

sql = """CREATE TABLE m3u8linkcheck (
         timecheck datetime,
         url text,
         status INT )"""
cursor.execute(sql)

#insert to table
try:
    cursor.execute("""INSERT INTO m3u8linkcheck VALUES (%s,%s)""",(2010-12-23,'http://google.co.th',1))
    db.commit()
except:
    db.rollback()

#show table
cursor.execute("""SELECT * FROM m3u8linkcheck;""")
print cursor.fetchall()
((188L, 90L),)

db.close()
