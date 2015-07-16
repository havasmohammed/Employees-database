#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host ="localhost", # your host, usually localhost
                     user = "root", # your username
                     passwd = "havas1993z", # your password
                     db = "Employees") # name of the data base
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("select employees.empno, employees.name, employees.designationid, \
	employees.salary, department_details.department from employees left join \
	department_details on employees.empno=department_details.empno")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row
cur.close()
