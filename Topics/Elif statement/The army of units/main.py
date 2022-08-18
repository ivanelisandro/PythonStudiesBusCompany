number = int(input())

if number < 1:
    print("no army")
elif number <= 9:
    print("few")
elif number <= 49:
    print("pack")
elif number <= 499:
    print("horde")
elif number <= 999:
    print("swarm")
else:
    print("legion")
