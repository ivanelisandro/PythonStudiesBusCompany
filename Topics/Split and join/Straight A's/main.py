grades = input().split()

a = [grade for grade in grades if grade == 'A']
proportion = len(a)/len(grades)

print(round(proportion, 2))
