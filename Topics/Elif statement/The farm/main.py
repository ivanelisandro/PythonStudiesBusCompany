animals = {
    'chicken': 23,
    'goat': 678,
    'pig': 1296,
    'cow': 3848,
    'sheep': 6769,
}

money = int(input())

affordable = {name: cost for (name, cost) in animals.items() if money >= cost}

if affordable:
    animal_name = max(affordable, key=lambda animal: affordable[animal])
    animal_cost = animals[animal_name]
    animal_quantity = money // animal_cost

    name_to_print = animal_name if animal_quantity == 1 or animal_name == 'sheep' else f'{animal_name}s'

    print(f'{animal_quantity} {name_to_print}')
else:
    print(None)
