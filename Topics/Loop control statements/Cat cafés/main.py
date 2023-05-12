cafes = {}

while True:
    next_cafe = input()
    if next_cafe == "MEOW":
        break

    (name, cats) = next_cafe.split()
    cafes[int(cats)] = name

selected_cafe = cafes[max(cafes)]
print(selected_cafe)
