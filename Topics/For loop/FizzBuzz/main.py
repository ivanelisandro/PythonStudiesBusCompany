for number in range(1, 101):
    part_1 = "Fizz" if number % 3 == 0 else ""
    part_2 = "Buzz" if number % 5 == 0 else ""
    part_3 = number if not part_1 and not part_2 else ""

    print(f"{part_1}{part_2}{part_3}")
