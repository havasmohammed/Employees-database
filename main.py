s = int(raw_input("enter the choice 1.employees basic details 2. To add designation_details"))
if s == 1:
	from employees import employees
	#from employees import selection
	from employees import join
elif s == 2:
	from designation_details import designation
	#from designation_details import selectiondes
	from designation_details import join

