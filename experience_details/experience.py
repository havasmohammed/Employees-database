import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
X = 'y'
try:
	#cursor object creation
	cursor = db.cursor()
	while X == 'y':
		empno = int(raw_input("Enter empno: "))
		level = raw_input( "Enter experience level: ")
		#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
		cursor.execute("Insert into experience_details Values (%s,%s)",(empno, level))
		X = raw_input("do u want to continue(y/n)")
except Exception as e:
	print str(e)
	db.commit()
cursor.close()
