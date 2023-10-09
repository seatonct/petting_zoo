from datetime import date
from animals import Donkey, Goat, Llama, MiniatureHorse
from animals import Sheep, GarterSnake, GreenSnake, KingSnake
from animals import RatSnake, Python, Catfish, Eel, StingRay, TigerShark, Tuna
from attractions import PettingZoo, SnakePit, Wetlands

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow", 1)
andy = Donkey("Andy", "donkey", "midday", "hay", 2)
gary = Goat("Gary", "goat", "midday", "grass", 3)
barry = Sheep("Barry", "sheep", "afternoon", "grass", 4)
lil_sebastian = MiniatureHorse(
    "Lil Sebastian", "miniature horse", "afternoon", "hay", 5)
brayden = RatSnake("Brayden", "rat snake", "rats", 6)
smithers = KingSnake("Smithers", "king snake", "snakes", 7)
lacy = GarterSnake("Lacy", "garter snake", "mice", 8)
alex = GreenSnake("Alex", "green snake", "bugs", 9)
snuggles = Python("Snuggles", "python", "rodents", 10)
ray = StingRay("Ray", "sting ray", "crustaceans", 11)
peter_the_eater = TigerShark("Peter the Eater", "tiger shark", "fish", 12)
bubba = Tuna("Bubba", "tuna", "kelp", 13)
wriggles = Eel("Wriggles", "eel", "algae", 14)
larry = Catfish("Larry", "catfish", "algae", 15)

varmint_village = PettingZoo(
    "Varmint Village", "critters that like to dig and scurry")
slither_inn = SnakePit(
    "The Slither Inn", "more snakes than an Indiana Jones movie")
critter_cove = Wetlands("Critter Cove", "aquatic wonders")

varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(andy)
varmint_village.add_animal(gary)
varmint_village.add_animal(barry)
varmint_village.add_animal(lil_sebastian)

slither_inn.add_animal(brayden)
slither_inn.add_animal(smithers)
slither_inn.add_animal(lacy)
slither_inn.add_animal(alex)
slither_inn.add_animal(snuggles)

critter_cove.add_animal(ray)
critter_cove.add_animal(peter_the_eater)
critter_cove.add_animal(bubba)
critter_cove.add_animal(wriggles)
critter_cove.add_animal(larry)

# print(varmint_village.last_critter_added)


# def attractions_report(attraction):
#     print(f"{attraction.name} is where you'll find {attraction.description}, like \n")

#     for animal in attraction.animals:
#         print(f"* {animal.name} the {animal.species}")

#     print("\n")


# attractions_report(varmint_village)
# attractions_report(slither_inn)
# attractions_report(critter_cove)

# print(f'{barry.name} the {barry.species} is available to pet during the {barry.shift} shift.')

# print(brayden)
# print(snuggles.feed())
# snuggles.slither()
# lil_sebastian.run()

for animal in varmint_village.animals:
    print(animal)
