# from sys import path
#
# path.append('..\\src')

""" game.py - runs the watermelon game\n
    run using 'python -m src.game'"""

from random import randrange
import src.logic #, src.words

# def game_round():
#
#     wordList = src.words.listSelector()
#     sliceCounter = 5
#     guessed = []
#     hiddenWord = wordList[randrange(0, len(wordList))]
#
#     src.logic.guesser(hiddenWord, guessed, sliceCounter, randGuess=True)
#     src.logic.guesser(hiddenWord, guessed, sliceCounter, randGuess=True)
#
#     print(hiddenWord)  # just for testing purposes
#
#     for char in hiddenWord:
#         if char in guessed:
#             print(char, end='')
#         else:
#             print('_', end='')
#     print()
#
#     while sliceCounter > 0:  # or not '_' in visibleWord:
#         sliceCounter = src.logic.guesser(hiddenWord, guessed, sliceCounter)
#
#         print('Slices Remaining:', sliceCounter)
#
#         if sliceCounter <= 0:
#             print('You Lost, the word was', hiddenWord)
#             break
#
#         winCheck = True
#         for char in hiddenWord:
#             if char in guessed:
#                 print(char, end='')
#             else:
#                 winCheck = False
#                 print('_', end='')
#         print()
#         if winCheck:
#             print("You Win!")
#             break

src.logic.run_round()