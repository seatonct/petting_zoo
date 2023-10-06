from datetime import date
from animal import Animal


class Python(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(
            f"""Some live {self.food} were placed in {self.name}'s enclosure for him to eat on {date.today().strftime("%m/%d/%Y")}.""")
