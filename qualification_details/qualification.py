import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
x='y'
while x=='y':
	designationid=int(raw_input("Enter designationid choices 1.441 2.442 3.443 4.444 5.445 6.446 "))
	qualification=raw_input( "Enter qualification: ")
	branch=raw_input( "Enter branch: ")
	#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
	cursor = db.cursor()
	cursor.execute("Insert into qualification_details Values (%s,%s,%s)",(designationid, qualification, branch))
	x=raw_input("do u want to continue(y/n)")
db.commit()
cursor.close()
