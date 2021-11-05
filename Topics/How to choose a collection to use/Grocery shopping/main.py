shopping_list = input().split()

count_items = {}

for item in shopping_list:
    if item not in count_items:
        count_items[item] = 0
    count_items[item] += 1

for key, value in count_items.items():
    print(value, key)
