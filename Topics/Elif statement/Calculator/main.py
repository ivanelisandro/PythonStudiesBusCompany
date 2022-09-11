invalid_division = "Division by 0!"


operations = {
    '+': (lambda a, b: a + b),
    '-': (lambda a, b: a - b),
    '*': (lambda a, b: a * b),
    'pow': (lambda a, b: a ** b),
    '/': (lambda a, b: invalid_division if b == 0 else a / b),
    'mod': (lambda a, b: invalid_division if b == 0 else a % b),
    'div': (lambda a, b: invalid_division if b == 0 else a // b),
}

first_number = float(input())
second_number = float(input())
operator = input()

print(operations[operator](first_number, second_number))
