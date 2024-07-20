import calendar

print(calendar.calendar(2024))
print(calendar.month(2024, 12))
primeiro_dia, ultimo_dia = calendar.monthrange(2024, 12)
print(calendar.day_name)
print(calendar.day_name[primeiro_dia])
print(calendar.weekday(2024, 12, 21))

for week in calendar.monthcalendar(2024, 12):
    for day in week:
        if day == 0:
            continue
        print(day)