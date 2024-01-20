import random
from paises import paises
import string

lives = '♥♥♥♥♥'
word = random.choice(paises).upper()

word_letters = set(word)
alphabet = set(string.ascii_uppercase)
used_letters = set()

while len(word_letters) > 0:
    print(f'your lives: {lives}')
    print('You have used these letters: ', ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input("Adivina una letra: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            lives = lives[1:]
            if len(lives) == 0:
                break
    elif user_letter in used_letters:
        print('You have already used that letter. Please try again')
    else:
        print('Invalid letter. Please try again')
        

word_list = [letter if letter in used_letters else '-' for letter in word]
print('The word is: ', word)

