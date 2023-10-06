from datetime import date
from walking import Donkey, Goat, Llama, Miniature_Horse, Sheep
from slithering import Garter_Snake, Green_Snake, King_Snake, Rat_Snake, Python
from swimming import Catfish, Eel, Sting_Ray, Tiger_Shark, Tuna
from attractions import PettingZoo, SnakePit, Wetlands

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
andy = Donkey("Andy", "donkey", "midday", "hay", 1)
gary = Goat("Gary", "goat", "midday", "grass")
barry = Sheep("Barry", "sheep", "afternoon", "grass")
lil_sebastian = Miniature_Horse(
    "Lil Sebastian", "miniature horse", "afternoon", "hay")
brayden = Rat_Snake("Brayden", "rat snake", "rats")
smithers = King_Snake("Smithers", "king snake", "snakes")
lacy = Garter_Snake("Lacy", "garter snake", "mice")
alex = Green_Snake("Alex", "green snake", "bugs")
snuggles = Python("Snuggles", "python", "rodents")
ray = Sting_Ray("Ray", "sting ray", "crustaceans")
peter_the_eater = Tiger_Shark("Peter the Eater", "tiger shark", "fish")
bubba = Tuna("Bubba", "tuna", "kelp")
wriggles = Eel("Wriggles", "eel", "algae")
larry = Catfish("Larry", "catfish", "algae")

varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("The Slither Inn")
critter_cove = Wetlands("Critter Cove")

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

# print(snuggles)
# print(snuggles.feed())
