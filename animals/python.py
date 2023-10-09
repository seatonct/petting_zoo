from datetime import date
from movements import Slithering
from .animal import Animal


class Python(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        print(
            f"""Some live {self.food} were placed in {self.name}'s enclosure for him to eat on {date.today().strftime("%m/%d/%Y")}.""")
