import MySQLdb   

db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",
db="Employees")
cursor = db.cursor()
designationid=int(raw_input("Enter designationid choices 1.441 2.442 3.443 4.444 5.445 6.446 "))
print "delete from designation_details where designationid=%d" %designationid
cursor.execute("delete from designation_details where designationid=%d" %designationid);
db.commit();
for row in cursor.fetchall():
    print row
cursor.close()
