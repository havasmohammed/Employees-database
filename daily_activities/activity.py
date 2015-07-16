import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
X = 'y'
try:
	#creation of cursor object
	cursor = db.cursor()
	while X == 'y':
		empno = int(raw_input( "Enter empno: "))
		date = raw_input( "Enter date: ")
		project = raw_input("Enter project: ")
		type = raw_input("Enter activitytype: ")
		description = raw_input("Enter activity description: ")
		timespent = int(raw_input( "Enter time spent: "))
		#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
		#insert into tables
		cursor.execute("Insert into daily_activities Values (%s,%s,%s,%s,%s,%s)",\
			(empno, date, project, type, description, timespent))
		X = raw_input("do u want to continue(y/n)")
except Exception as e:
	print str(e)
	db.commit()
cursor.close()
