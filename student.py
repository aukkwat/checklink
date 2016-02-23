import MySQLdb

def main():

  # Connect to the MySQL database
  db = MySQLdb.connect(host = '10.211.55.30', user = 'root', \
       passwd = 'bigmaster', db = 'checklink', port = 3308)

  # Creation of a cursor
  cursor = db.cursor()

  # Execution of a SQL statement
  cursor.execute ("select * from student")

  # Get the total number of rows
  numrows = int (cursor.rowcount)
  print "numrows = ", numrows

  # Get and display the rows one at a time
  for i in range (numrows):
    row = cursor.fetchone()
    if (row):
      print row[0], row[1], row[2], row[3]

  # Execution of an insert SQL statement
  cursor.execute ("insert into student (lastName, firstName, major, \
  bDay) values ('Mouse', 'Mickey', 'Dance', '1928-11-18')")

  # Check that the insert operation worked
  print
  print "Check Insert Operation"
  cursor.execute ("select * from student")
  numrows = int (cursor.rowcount)
  for i in range (numrows):
    row = cursor.fetchone()
    if (row):
      print row[0], row[1], row[2], row[3]

  # # Execution of an update SQL statement
  # cursor.execute ("update student set major = 'Acting' where \
  # lastName = 'Mouse' and firstName = 'Mickey'")
  #
  # # Check that the update operation worked
  # print
  # print "Check Update Operation"
  # cursor.execute ("select * from student")
  # numrows = int (cursor.rowcount)
  # for i in range (numrows):
  #   row = cursor.fetchone()
  #   if (row):
  #     print row[0], row[1], row[2], row[3]

  # # Execution of a delete SQL statement
  # cursor.execute ("delete from student where lastName = 'Mouse' and \
  # firstName = 'Mickey'")
  #
  # # Check that the delete operation worked
  # print
  # print "Check Delete Operation"
  # cursor.execute ("select * from student")
  # numrows = int (cursor.rowcount)
  # for i in range (numrows):
  #   row = cursor.fetchone()
  #   if (row):
  #     print row[0], row[1], row[2], row[3]

  # Close the cursor
  cursor.close()

main()
