class Wetlands:

    def __init__(self, name):
        self.name = name
        self.description = "Gatlinburg's only one-acre walk-through wetlands and wet bar, full of feathered friends and fantastic fish"
        self.animals = list()

    def __str__(self):
        return f"{self.name} is {self.description}."

    def add_animal(self, animal):
        return self.animals.append(animal)
