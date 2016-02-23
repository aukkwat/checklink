import MySQLdb
#connect to db
db = MySQLdb.connect(host = '10.211.55.30',user = 'root',passwd = 'bigmaster',db = 'checklink',port = 3308)

#setup cursor
cursor = db.cursor()

cursor.execute("""INSERT INTO m3u8linkcheck VALUES (%s,%s)""",(2010-12-23,'http://google.co.th',1))
db.commit()
