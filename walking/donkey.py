from datetime import date


class Donkey:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.walking = True
        self.shift = shift
        self.food = food
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species}, who eats {self.food} and works the {self.shift} shift."

    def feed(self):
        print(
            f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
