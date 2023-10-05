from datetime import date


class Catfish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.food = food
        self.date_added = date.today()

    def __str__(self):
        return f"{self.name} is a {self.species} who eats {self.food}."

    def feed(self):
        print(
            f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.')
