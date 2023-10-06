from datetime import date
from animal import Animal


class Goat(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}, who eats {self.food} and works the {self.shift} shift."
