import random

flowers = ["LILAC", "COSMOS", "GERANIUM", "IRIS", "DAFFODIL", "TULIP", "MARIGOLD", "ZINNIA", "PEONY", "ROSE", "MORNING GLORY", "PETUNIA", "PANSY", "ALYSSUM", "VIOLET", "LILY OF THE VALLEY", "SNAPDRAGON", "GARDENIA", "ORCHID"]

selection = random.choice(flowers)
answer = selection

jumble = list(selection)

for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,

guess = raw_input("\nUnscramble the letters to spell out a type of flower.\n")
guess = guess.upper()

while guess != answer:
    guess = raw_input("\nNot quite...Try again!\n")
    guess = guess.upper()
else:
    print ("YES! You guessed it! Great job!")
