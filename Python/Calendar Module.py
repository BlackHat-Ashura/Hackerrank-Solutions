import calendar

mm, dd, yyyy = list(map(int,input().split()))

day_index = calendar.weekday(year=yyyy, month=mm, day=dd)
day = calendar.day_name[day_index].upper()
print(day)
