import MySQLdb   
db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",db="Employees")
X = 'y'
try:
	cursor = db.cursor()
	while X == 'y':
		print "enter the designationid from the list"
		cursor.execute("select * from designation_details")
		for row in cursor.fetchall():
			print "designationid: %d,designation: %s"%(row[0],row[1])
		designationid=int(raw_input())
		qualification = raw_input( "Enter qualification: ")
		branch = raw_input( "Enter branch: ")
		#db= pyodbc.connect('DRIVER={SQL Server};SERVER=localhoast;DATABASE=tutorial')
		cursor.execute("Insert into qualification_details Values (%s,%s,%s)",(designationid, qualification, branch))
		X = raw_input("do u want to continue(y/n)")
except Exception as e:
	print str(e)
	db.commit()
cursor.close()
