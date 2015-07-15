import MySQLdb   

db = MySQLdb.connect(host="localhost", user="root",passwd="havas1993z",
db="Employees")
cursor = db.cursor
designationid=int(raw_input("please enter the empno: "))
print "delete from daily_activities where empno=%d" %empno
cursor.execute("delete from daily_activities where empno=%d" %empno);
db.commit();
for row in cursor.fetchall():
    print row
cursor.close()
