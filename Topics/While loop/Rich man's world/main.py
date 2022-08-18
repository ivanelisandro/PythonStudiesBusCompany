deposit = int(input())
years = 0

while deposit < 700000:
    years += 1
    deposit = deposit * 1.071

print(years)
