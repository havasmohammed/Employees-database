import MySQLdb   

db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",
db="Employees")
cursor = db.cursor()
designationid=int(raw_input("please enter the designationid: "))
print "delete from designation_details where designationid=%d" %designationid
cursor.execute("delete from designation_details where designationid=%d" %designationid);
db.commit();
for row in cursor.fetchall():
    print row
