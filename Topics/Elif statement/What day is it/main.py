offset = int(input())

reference = 10.5
full_day = 24
new_time = reference + offset

if new_time < 0:
    print("Monday")
elif 0 <= new_time <= full_day:
    print("Tuesday")
else:
    print("Wednesday")