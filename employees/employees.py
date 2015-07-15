import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
x='y'
while x=='y':
	empno=int(raw_input( "Enter empno: "))
	name=raw_input( "Enter name: ")
	age=int(raw_input("Enter age: "))
	designationid=int(raw_input("Enter designationid choices 1.441 2.442 3.443 4.444 5.445 6.446 "))
	salary=int(raw_input("Enter salary: "))
	#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
	cursor = db.cursor()
	cursor.execute("Insert into employees Values (%s,%s,%s,%s,%s)",( name, age, designationid, salary, empno))
	x=raw_input("do u want to continue(y/n)")
db.commit()
cursor.close()
