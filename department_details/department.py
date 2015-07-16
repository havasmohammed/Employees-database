import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root", passwd="havas1993z",db="Employees")
X = 'y'
try:
	#creation of cursor object
	cursor = db.cursor()
	while X == 'y':
		empno = int(raw_input("Enter empno: "))
		department = raw_input( "Enter department: ")
		#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
		cursor.execute("Insert into department_details Values (%s, %s)",\
			(empno, department))
		X = raw_input("do u want to continue(y/n)")
except Exception as e:
	print str(e)
	db.commit()
cursor.close()
