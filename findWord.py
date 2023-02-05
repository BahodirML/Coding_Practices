from uzwords import words
import random


guessed_word = random.choice(words)
# print(guessed_word)
display = ['_'] * len(guessed_word)



def find_word():
    while '_' in display:
        print(''.join(display))
        guess = input('Enter the letter')

        if guess in guessed_word:
            print(f"Yes the letter {guess} exists in the wword.")
            for i in range(len(guessed_word)):
                if guessed_word[i] == guess: 
                    display[i] = guess
        else:
            print(f"Sorry, the letter {guess} does not exist in the word")
    print('Congratulations you have succesfully found the word, it is ', guessed_word)

find_word()