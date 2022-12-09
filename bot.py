from lists import CHARACTERS, EFFECTS, STYLES, LOCATIONS
import random

character = random.choice(CHARACTERS)
location = random.choice(LOCATIONS)
effect = random.choice(EFFECTS)
style = random.choice(STYLES)

prompt = f"{character} {location}, {effect}, {style}"
print(prompt)
