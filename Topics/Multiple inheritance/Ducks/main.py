class Animal:
    def __init__(self):
        self.name = "Animal"


class FlyingAnimal(Animal):
    def __init__(self):
        super().__init__()
        self.name = "FlyingAnimal"


class SwimmingAnimal(Animal):
    def __init__(self):
        super().__init__()
        self.name = "SwimmingAnimal"


class WalkingAnimal(Animal):
    def __init__(self):
        super().__init__()
        self.name = "WalkingAnimal"


class Duck(FlyingAnimal, SwimmingAnimal, WalkingAnimal):
    def __init__(self):
        super().__init__()
        self.name = "Duck"
