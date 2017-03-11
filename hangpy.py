"""
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
hangpy.py
Created on 2017-03-11T16:28:00Z
@author:Joshua Hu
"""
from __future__ import print_function

if __name__ == '__main__':
    entered_word = False
    while not entered_word:
        try:
            word = raw_input("What's the word to guess?: ")
            target_word = list(str(word))
            entered_word = True
        except:
            print("Words")

        guess_word = ['' for x in xrange(len(target_word))]

    entered_lives = False
    while not entered_lives:
        try:
            lives = int(raw_input("How many lives?:"))
            entered_lives = True
        except ValueError:
            print("Please enter a number.")

    game_won = False
    while lives > 0 and game_won == False:
        try:
            guess = raw_input("Guess a letter: ")

            if guess in target_word:
                print("Letter guessed.")
                location = target_word.index(guess)
                guess_word[location] = guess

                if guess_word == target_word:
                    print("You won!\nWord: " , ''.join(target_word))
                    game_won = True

            else:
                lives -= 1
                print("Wrong guess.\n" + str(lives) + " lives left.")
        except:
            print("Error.")

    print("Game over.")
