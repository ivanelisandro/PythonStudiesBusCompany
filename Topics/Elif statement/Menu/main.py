menu = {
    'pizza': 'Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy',
    'salad': 'Caesar salad, Green salad, Tuna salad, Fruit salad',
    'soup': 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup',
}

selection = input()

if selection in menu:
    print(menu[selection])
else:
    print("Sorry, we don't have it in the menu")
