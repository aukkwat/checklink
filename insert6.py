import MySQLdb
name="XYZ"
number="123456"
db=MySQLdb.Connect("10.211.55.30","root","bigmaster","checklink")
cursor=db.cursor()

sql= ("""INSERT INTO phonebook(number, Mobile) VALUES("%s","%s")""",name,number)
cursor.execute(sql)
db.commit()
db.close()
