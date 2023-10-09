from .attraction import Attraction


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    @property
    def last_critter_added(self):
        return f"{self.animals[-1].name} the {self.animals[-1].species}"
