colors = {
    'Purple': (160, 32, 255),
    'Light Blue': (80, 208, 255),
    'Yellow': (255, 224, 32),
}

selection = input()

if selection in colors:
    print(colors[selection])
