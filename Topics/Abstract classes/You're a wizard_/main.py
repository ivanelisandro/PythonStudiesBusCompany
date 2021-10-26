from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, rank, level):
        self.name = name
        self.rank = rank
        self.level = level
        super().__init__()

    @abstractmethod
    def fight(self):
        pass

    @abstractmethod
    def do_spell(self):
        pass

    def sing_song(self):
        print("No songs for me!")


class Wizard(Player):
    def fight(self):
        self.do_spell()

    def do_spell(self):
        print("Expecto patronum!")
