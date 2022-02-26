import datetime

datesr=input("Ingrese una fecha en el formado 'DD/MM/AA': ")
date = datetime.strptime(datesr,'%d/%m/$y')
print (date)

'''
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
print (NextDay_Date)



from datetime import datetime

date_time_str = '180919 015519'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')


print "The type of the date is now",  type(date_time_obj)
print "The date is", date_time_obj
'''