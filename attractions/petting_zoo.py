class PettingZoo:

    def __init__(self, name):
        self.name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def __str__(self):
        return f"{self.name} has {self.description}."

    def add_animal(self, animal):
        return self.animals.append(animal)

    @property
    def last_critter_added(self):
        return f"{self.animals[-1].name} the {self.animals[-1].species}"
