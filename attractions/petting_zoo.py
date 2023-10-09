from movements import Walking
from .attraction import Attraction


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(
                f'{animal} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')

    def add_animal_type_check(self, animal):
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(
                f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.attraction_name} attraction.')

    @property
    def last_critter_added(self):
        return f"{self.animals[-1].name} the {self.animals[-1].species}"
