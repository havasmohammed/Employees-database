import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
x='y'
while x=='y':
	designationid=int(raw_input("Enter designationid: "))
	department=raw_input( "Enter department: ")
	#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
	cursor = db.cursor()
	cursor.execute("Insert into department_details Values (%s,%s)",(designationid, department))
	x=raw_input("do u want to continue(y/n)")
db.commit()
