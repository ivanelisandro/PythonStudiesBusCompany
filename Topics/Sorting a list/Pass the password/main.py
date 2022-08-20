# the following line reads the list from the input, do not modify it, please
passwords = input().split()

passwords.sort(key=len)
for password in passwords:
    print(password, len(password))
