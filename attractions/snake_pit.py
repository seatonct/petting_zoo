class SnakePit:

    def __init__(self, name):
        self.name = name
        self.description = "more snakes than an Indiana Jones movie"
        self.animals = list()

    def __str__(self):
        return f"{self.name} has {self.description}."

    def add_animal(self, animal):
        return self.animals.append(animal)
