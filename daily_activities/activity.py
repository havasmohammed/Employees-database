import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
x='y'
while x=='y':
	designationid=int(raw_input( "Enter designationid: "))
	date=raw_input( "Enter date: ")
	project=raw_input("Enter project: ")
	type=raw_input("Enter activitytype: ")
	description=raw_input("Enter activity description: ")
	timespent=int(raw_input( "Enter time spent: "))
	#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
	cursor = db.cursor()
	cursor.execute("Insert into daily_activities Values (%s,%s,%s,%s,%s,%s)",(designationid, date, project, type, description, timespent))
	x=raw_input("do u want to continue(y/n)")
db.commit()
