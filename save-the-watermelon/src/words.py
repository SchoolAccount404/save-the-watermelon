#!/usr/bin/env python3

""" logic.py - watermelon hangman words handler

    you just run listSelector(), and get back whichever list the user picked"""

from src.logic import input_val



def listSelector():
    listDict = {'fruits': ['apple', 'orange', 'pear', 'banana', 'watermelon', 'cantaloupe', 'cherry', 'durian', 'mango', 'peach', 'pomegranate'],
                'test': ['lorem', 'ipsum', 'dolor']}
    # chosenList = input('Select a category:\n' + '\n'.join(list(listDict.keys())) + '\n')
    chosenList = input_val('Select a category:\n' + '\n'.join(list(listDict.keys())) + '\n', 'Invalid input',listDict.keys(), False)
    return listDict[chosenList]
