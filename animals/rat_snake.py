from datetime import date
from movements import Slithering
from .animal import Animal


class RatSnake(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        print(
            f'{self.name} was fed live {self.food} on {date.today().strftime("%m/%d/%Y")}.')
