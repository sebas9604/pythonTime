import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low')
        elif guess > random_number:
            print('Too high')
    print('Congratulations!!')

def computer_guess():
    
    finish = ''
    low = 1
    high = 1000
    while finish != 'c':
        number = random.randint(low, high)
        finish = input(f'Is {number} too High (h), too low (l) or Correct (c): ')

        if finish == 'h':
            high = number - 1
        elif finish == 'l':
            low = number + 1
    
    print('Great!!')
if __name__ == '__main__':
    #x = int(input("Ingrese un numero: "))
    computer_guess()