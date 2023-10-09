from datetime import date
from movements import Walking
from .animal import Animal


class Llama(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def __str__(self):
        return f"{self.name} is a {self.species}, who eats {self.food} and works the {self.shift} shift."

    def feed(self):
        print(
            f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")} after being serenaded with "Rocky Top."')
