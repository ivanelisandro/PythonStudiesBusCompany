rooms = [int(input()), int(input()), int(input())]
desks = 0
students_per_desk = 2

for students in rooms:
    desks += students // students_per_desk
    if students % students_per_desk > 0:
        desks += 1

print(desks)
