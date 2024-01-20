import random

pc = random.randint(1,3)

match pc:
    case 1:
        pc = 'rock'
    case 2:
        pc = 'paper'
    case 3:
        pc = 'scissors'
user = ''

while user != 0:
    print('------NEW GAME------')
    user = int(input("Rock (1)\nPaper (2)\nScissors (3)\nExit (0)\n .."))

    if user == 1:
        if pc == 1:
            print('Tie')
        elif pc == 2:
            print('You lose')
        else:
            print('You Win!!')
    elif user == 2:
        if pc == 1:
            print('You Win!!')
        elif pc == 2:
            print('Tie')
        else:
            print('You Lose')
    elif user == 3:
        if pc == 1:
            print('You Lose')
        elif pc == 2:
            print('You Win!!')
        else:
            print('Tie')
    else:
        if user != 0:
            print('Select a correct option')     