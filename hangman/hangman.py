import random

from hang import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word: 
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #saves all the correct letters in the word as a set
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #keeping what the user has guessed as a set

    #setting a number a lives
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        #letters used
        #' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, "life(s) left and you have used these letters: ", ' '.join(used_letters))

        #what the current word is (ie W -- R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))
    
        #getting user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 #subtracts from life
                print('letter is not in the word.')
        elif user_letter in used_letters:
            print("You have guessed this before")
        else:
            print("Invalid character, try again")

    if lives == 0:
        print('You died, sorry. The word was ', word)
     
    print("You guessed the word", word, '!!' )

    



hangman()