import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
x='y'
while x=='y':
	designationid=int(raw_input("Enter designationid: "))
	designation=raw_input( "Enter designation: ")
	#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
	cursor = db.cursor()
	cursor.execute("Insert into designation_details Values (%s,%s)",(designationid, designation))
	x=raw_input("do u want to continue(y/n)")
db.commit()
