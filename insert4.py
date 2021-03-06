import MySQLdb

# Open database connection
db = MySQLdb.connect(host="10.211.55.30",    # your host, usually localhost
                     user="root",         # your username
                     passwd="bigmaster",  # your password
                     db="checklink",      # name of the data base
                     port=3306)        # port if tge data base

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO m3u8checklink(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
