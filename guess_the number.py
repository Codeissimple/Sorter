#guessing the number game
import random

number = random.randint(1,20)
guess = int(input("Guess the number I'm thinking of, between 1 to 20"))
if guess != int:
    print('wrong inut type, enter number /n')

while guess != number:
    print("Sorry, you didn't guess")
    guess = int(input("try again"))