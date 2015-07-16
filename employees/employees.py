import MySQLdb  
#name of the host, user, password and database 
db = MySQLdb.connect(host="localhost", user="root", passwd="havas1993z", db="Employees")
X='y'
try:
	#cursor object creation
	cursor = db.cursor()
	while X == 'y':
		empno = int(raw_input( "Enter empno: "))
		name = raw_input( "Enter name: ")
		age = int(raw_input("Enter age: "))
		print "enter the designationid from the list"
		cursor.execute("select * from designation_details")
		for row in cursor.fetchall():
			print "designationid: %d,designation: %s"%(row[0],row[1])
		designationid = int(raw_input())
		salary = int(raw_input("Enter salary: "))
		#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
		cursor.execute("Insert into employees Values (%s, %s, %s, %s, %s)",\
			( name, age, designationid, salary, empno))
		X = raw_input("do u want to continue(y/n)")
except Exception as e:
	print str(e)
	db.commit()
cursor.close()
