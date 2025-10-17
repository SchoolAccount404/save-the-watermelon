#!/usr/bin/env python3

""" logic.py - watermelon hangman functions

    input_val() is an advanced version of input()
    \nguesser() needs to have its first three arguments be (hiddenWord, guessed, sliceCounter), the fourth, randGuess, makes it silently make a new correct guess, rather than using the user's guess
    \ngame_round() needs no arguments, pretty self explanatory name
    \nrun_round() is what you should generally be using to start it though, otherwise it wont ask if you want to play again """

from string import ascii_letters
from random import randrange


# input validation
# accounts for all weird input as far as I can tell
# prompt and failtext are just visual
# incheck is what it makes sure that the user input is in, or else makes them give a new input until it is
# uselen just controls whether it checks that the input is a single character, or else makes them give a new input until it is
def input_val(prompt='Error, no prompt given', failtext='Invalid input', incheck=ascii_letters, uselen=True):
    userInput = input(prompt).lower()
    while userInput not in incheck or (uselen and len(userInput) != 1): # the len() bit is important because otherwise it could accept 'ab' or 'efgh' under default settings
        print(failtext)
        userInput = input(prompt).lower()
    return userInput

def guesser(hiddenWord, guessed, sliceCounter, randGuess=False):
    if not randGuess:
        guess = input_val('Enter your guess: ', 'Your guess must be a single letter.')
    else:
        guess = hiddenWord[randrange(0, len(hiddenWord))]
        while guess in guessed:
            guess = hiddenWord[randrange(0, len(hiddenWord))]

    if guess in hiddenWord:
        if guess not in guessed:
            if not randGuess:
                print('Good guess!')
            guessed.append(guess)
        elif not randGuess:
            print('You already guessed', guess, 'and it was correct.')

    elif guess not in guessed:
        if not randGuess:
            print('Incorrect guess.')
        guessed.append(guess)
        sliceCounter -= 1
    elif not randGuess:
        print('You already guessed', guess, 'and it was incorrect.')

    return sliceCounter

import src.words # imported down here because it messed with words.py trying to use input_val

def game_round():

    wordList = src.words.listSelector()
    sliceCounter = 5
    guessed = []
    hiddenWord = wordList[randrange(0, len(wordList))]

    guesser(hiddenWord, guessed, sliceCounter, randGuess=True)
    guesser(hiddenWord, guessed, sliceCounter, randGuess=True)

    #print(hiddenWord)  # just for testing purposes

    for char in hiddenWord:
        if char in guessed:
            print(char, end='')
        else:
            print('_', end='')
    print()

    while sliceCounter > 0:  # or not '_' in visibleWord:
        sliceCounter = guesser(hiddenWord, guessed, sliceCounter)

        print('Slices Remaining:', sliceCounter)

        if sliceCounter <= 0:
            print('You Lost, the word was', hiddenWord)
            break

        winCheck = True
        for char in hiddenWord:
            if char in guessed:
                print(char, end='')
            else:
                winCheck = False
                print('_', end='')
        print()
        if winCheck:
            print("You Win!")
            break

def run_round():
    game_round()
    while input_val('Do you want to play again? (y/n): ', 'Enter either y or n', 'yn').lower() == 'y':
        game_round()

if __name__ == '__main__':
    print('logic running as main')