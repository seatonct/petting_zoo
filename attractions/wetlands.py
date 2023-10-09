from movements import Swimming
from .attraction import Attraction


class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(
                f'{animal} is not an aquatic animal, so please do not put it in the {self.attraction_name} attraction.')

    def add_animal_type_check(self, animal):
        if isinstance(animal, Swimming):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(
                f'{animal} is not an aquatic animal, so please do not try to put it in the {self.attraction_name} attraction.')
