from datetime import date
from .animal import Animal


class Rat_Snake(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(
            f'{self.name} was fed live {self.food} on {date.today().strftime("%m/%d/%Y")}.')
