import random, sys
print("Rock, Paper, Scissors")

# these variables keep track of the number of wins, losses, and ties.
wins = 0
losses =0
ties = 0

while True: #the main game loop
    print('Enter your move: (r)ock, (p)aper, or (s)cissors:')
    playerMove = input()
    if playerMove == 'q':
        sys.exit() #quit the program
    if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
        break
    print('Type one of r,p,s, or q.')
# Display what the player chose:
if playerMove == 'r':
    print('ROCK VS ...')
elif playerMove == 'p':
    print('PAPER VS...')
elif playerMove == 's':
    print('SCISSORS VS ...')
# Display what computer chose
randomNumber = random.randint(1,3)
if randomNumber == 1:
    computerMove = 'r'
    print('ROCK')
elif randomNumber == 2:
    computerMove = 'p'
    print('PAPER')
elif randomNumber == 3:
    computerMove = 's'
    print('SCISSORS')
# Display and record the win/loss/tie
if playerMove == computerMove:
    print('Draw')
elif playerMove == 'r' and computerMove == 's':
    print('You win!')
    wins =+ 1
elif playerMove == 'p' and computerMove == 'r':
    print('You win!')
    wins =+ 1
elif playerMove == 's' and computerMove == 'p':
    print('You win!')
    wins =+1
elif playerMove == 'r' and computerMove == 'p':
    print('You lose!')
    losses =+ 1
elif playerMove == 'p' and computerMove == 's':
    print('You lose!')
    losses =+1
elif playerMove == 's' and computerMove == 'r':
    print('You lose!')
    losses =+ 1

