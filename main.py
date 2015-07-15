s=int(raw_input("enter the choice 1.emoployees 2.designation_details 3.qualification_details 4.daily_activities "))
if s==1:
	from employees import employees
	#from employees import selection
	from employees import join
elif s==2:
	from designation_details import designation
	from designation_details import selectiondes
	from designation_details import join
elif s==3:
	from qualification_details import qualification
	from qualification_details import selectionqua
	from qualification_details import joinqua  
else:
	from daily_activities import activity
	from daily_activities import selectionact
