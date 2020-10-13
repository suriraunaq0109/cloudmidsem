import calendar
y = 2020
m = 10
print(calendar.month(y, m))
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M"))