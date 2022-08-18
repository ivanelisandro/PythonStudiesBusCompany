#  write your code here 
with open('.\\data\\dataset\\input.txt', mode='r') as file:
    lines = file.readlines()
    print(lines.count('summer\n'))
