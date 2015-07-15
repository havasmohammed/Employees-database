import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
x='y'
while x=='y':
	empno=int(raw_input("Enter empno: "))
	level=raw_input( "Enter experience level: ")
	#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
	cursor = db.cursor()
	cursor.execute("Insert into experience_Details Values (%s,%s)",(empno, level))
	x=raw_input("do u want to continue(y/n)")
db.commit()
cursor.close()
