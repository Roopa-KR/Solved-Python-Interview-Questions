import calendar
month,day,year=map(int,input().split())
date_num=calendar.weekday(year,month,day)
print(calendar.day_name[date_num].upper())