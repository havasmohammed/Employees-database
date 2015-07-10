import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
x='y'
while x=='y':
	empno=int(raw_input( "Enter empno: "))
	name=raw_input( "Enter name: ")
	age=int(raw_input("Enter age: "))
	designationid=int(raw_input("Enter designationid: "))
	salary=int(raw_input("Enter salary: "))
	#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
	cursor = db.cursor()
	cursor.execute("Insert into basic_details Values (%s,%s,%s,%s,%s)",(empno, name, age, designationid, salary))
	x=raw_input("do u want to continue(y/n)")
db.commit()
