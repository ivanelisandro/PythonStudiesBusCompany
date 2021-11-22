def calculate_fill(index):
    a = 1
    b = 2
    return a + b * index


def calculate_blank(used_space, max_space):
    b = 2
    return int((max_space - used_space) / b)


height = int(input())
max_fill = calculate_fill(height - 1)

for n in range(0, height):
    fill_number = calculate_fill(n)
    fill = '#' * fill_number
    blank = ' ' * calculate_blank(fill_number, max_fill)
    print(blank, fill, blank, sep='')
