import MySQLdb, string

def main():

  # Connect to the MySQL database
  db = MySQLdb.connect(host = '10.211.55.30', user = 'root', \
       passwd = 'bigmaster', db = 'checklink', port = 3308)

  # Check if connection was successful
  if (db):
    print "Connection successful"
    print
  else:
    return

  # Creation of a cursor
  cursor = db.cursor()

  # Define variables
  table = 'student'

  # Execution of a parameterized SQL statement
  cursor.execute ("select * from %s" % (table))

  # Get the total number of rows
  numrows = int (cursor.rowcount)
  print "numrows = ", numrows

  # Get and display the rows one at a time
  for i in range (numrows):
    row = cursor.fetchone()
    if (row):
      print row[0], row[1], row[2], row[3]

  # Define variables
  lastName = 'Mouse'
  firstName = 'Mickey'
  major = 'Dance'
  bDay = '1928-11-18'

  # Execution of an insert SQL statement
  cursor.execute ("""insert into student (lastName, firstName, major, bDay)
  values (%s, %s, %s, %s)""", (lastName, firstName, major, bDay))

  # Check that the insert operation worked
  print
  print "Check Insert Operation"
  cursor.execute ("select * from student")
  numrows = int (cursor.rowcount)
  print "numrows = ", numrows
  for i in range (numrows):
    row = cursor.fetchone()
    if (row):
      print row[0], row[1], row[2], row[3]

  # Read data from a file
  data = []
  infile = open ("name.txt", "r")
  for line in infile:
    line = line.rstrip("\n")
    line = line.strip()
    seq = line.split()
    seq = tuple (seq)
    data.append(seq)
  infile.close()

  # Multiple execution of insert SQL statement
  cursor.executemany ("""insert into student (lastName, firstName, major,
  bDay) values (%s, %s, %s, %s)""", data)

  # Get all the rows at once
  print
  print "Getting all the rows at once for multiple entry"
  cursor.execute ("select * from student")
  result_set = cursor.fetchall()
  for record in result_set:
    print record[0], record[1], record[2], record[3]

  # Execution of an update SQL statement
  newMajor = 'Acting'
  cursor.execute ("""update student set major = %s where
  lastName = 'Mouse' and firstName = 'Mickey'""", (newMajor))

  # Check that the update operation worked
  print
  print "Check Update Operation"
  cursor.execute ("select * from student")
  numrows = int (cursor.rowcount)
  for i in range (numrows):
    row = cursor.fetchone()
    if (row):
      print row[0], row[1], row[2], row[3]

  # Execution of a delete SQL statement
  cursor.execute ("delete from student where lastName = 'Mouse'")
  cursor.execute ("delete from student where lastName = 'Duck' and \
  firstName != 'Donald'")

  # Check that the delete operation worked
  print
  print "Check Delete Operation"
  cursor.execute ("select * from student")
  numrows = int (cursor.rowcount)
  for i in range (numrows):
    row = cursor.fetchone()
    if (row):
      print row[0], row[1], row[2], row[3]

  # Close the cursor
  cursor.close()

main()
