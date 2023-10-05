from datetime import date
from walking import Donkey, Goat, Llama, Miniature_Horse, Sheep
from slithering import Garter_Snake, Green_Snake, King_Snake, Rat_Snake, Python
from swimming import Catfish, Eel, Sting_Ray, Tiger_Shark, Tuna

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
andy = Donkey("Andy", "donkey", "midday", "hay")
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

print(f'{barry.name} the {barry.species} is available to pet during the {barry.shift} shift.')

print(snuggles)
print(snuggles.feed())
