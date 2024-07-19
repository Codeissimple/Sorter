#guessing the number game
import random

secretNumber = random.randint(1,20)
print("I'm thinking of a number between 1 and 20")

# Ask the player to guess 6 times
for guessesTaken in range(1,7):
