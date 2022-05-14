import calendar
def weekday(day,month,year):
    
	dayNumber = calendar.weekday(year, month, day)
	days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	return (days[dayNumber])

date = int(input())
month = int(input())
year = int(input())
print(weekday(date,month,year))