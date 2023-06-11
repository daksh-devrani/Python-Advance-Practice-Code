from datetime import *
print(datetime.now()) #to print current time
print(datetime.now(timezone.utc)) #for universal time
today= datetime.now(timezone.utc)
tommorow= today + timedelta(days=1)  #for time difference
print(today)
print(tommorow)

print(today.strftime('%d/%m/%Y %H:%M'))  #for String formate time i.e. formating how the date and time is shown
user_date=input('enter date in YYYY-MM-DD format: ')
date_1=datetime.strptime(user_date, '%Y-%m-%d') #for formating a string into a date time(string parse time)