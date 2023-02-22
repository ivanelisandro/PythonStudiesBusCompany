pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

cook_book = {
    'pasta': pasta,
    'apple pie': apple_pie,
    'ratatouille': ratatouille,
    'chocolate cake': chocolate_cake,
    'omelette': omelette}

ingredient = input()

for key, value in cook_book.items():
    if ingredient in value:
        print(f'{key} time!')
