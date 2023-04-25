taxes = (
    (132407, 28),
    (42708, 25),
    (15528, 15),
    (0, 0),
)

income = int(input())
percent = 0

for key, tax in taxes:
    if income >= key:
        percent = tax
        break

calculated_tax = round(income * percent / 100)
print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")