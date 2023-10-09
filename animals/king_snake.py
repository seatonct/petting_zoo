from datetime import date
from movements import Slithering
from .animal import Animal


class KingSnake(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
