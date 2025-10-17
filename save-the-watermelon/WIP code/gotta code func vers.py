from random import randrange
from string import ascii_letters


def game_round():
    # wordList = ['apple','orange','pear','banana','watermelon','cantaloupe','cherry','durian','mango','peach','pomegranate']
    wordList = listSelector()
    sliceCounter = 5
    guessed = []
    hiddenWord = wordList[randrange(0, len(wordList))]

    guesser(hiddenWord, guessed, sliceCounter, randGuess=True)
    guesser(hiddenWord, guessed, sliceCounter, randGuess=True)

    # winCheck = False
    # visibleWord = '_' * len(hiddenWord)

    print(hiddenWord)  # just for testing purposes
    # print('_' * len(hiddenWord))
    for char in hiddenWord:
        if char in guessed:
            print(char, end='')
        else:
            print('_', end='')
    print()

    while sliceCounter > 0:  # or not '_' in visibleWord:
        # print(visibleWord)
        # guess = input_val('Enter your guess: ','Your guess must be a single letter.')
        sliceCounter = guesser(hiddenWord, guessed, sliceCounter)
        # guess = input('Enter your guess: ').lower()
        # if guess not in ascii_letters or len(guess) != 1:
        #     print('Invalid input')
        #     continue

        # if guess in hiddenWord:
        #     if guess not in guessed:
        #         print('Good guess!')
        #         guessed.append(guess)
        #         # for i in range(0,len(hiddenWord)):
        #         #     if hiddenWord[i] in guessed:
        #         #         visibleWord[i] = guess
        #     else:
        #         print('You already guessed', guess, 'and it was correct.')
        # elif guess not in guessed:
        #     print('Incorrect guess.')
        #     guessed.append(guess)
        #     sliceCounter -= 1
        # else:
        #     print('You already guessed', guess, 'and it was incorrect.')

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


def input_val(prompt='Error, no prompt given', failtext='Invalid input', incheck=ascii_letters, uselen=True):
    userInput = input(prompt).lower()
    while userInput not in incheck or (uselen and len(userInput) != 1):
        print(failtext)
        userInput = input(prompt).lower()
    return userInput
# copied to logic.py

def listSelector():
    listDict = {'fruits': ['apple', 'orange', 'pear', 'banana', 'watermelon', 'cantaloupe', 'cherry', 'durian', 'mango',
                           'peach', 'pomegranate'],
                'test': ['lorem', 'ipsum', 'dolor']}
    # chosenList = input('Select a category:\n' + '\n'.join(list(listDict.keys())) + '\n')
    chosenList = input_val('Select a category:\n' + '\n'.join(list(listDict.keys())) + '\n', 'Invalid input',
                           listDict.keys(), False)
    return listDict[chosenList]
# copied to words.py

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
            # for i in range(0,len(hiddenWord)):
            #     if hiddenWord[i] in guessed:
            #         visibleWord[i] = guess
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
# copied to logic.py

#print(listSelector())


game_round()
# while input('Do you want to play again? (y/n): ').lower() == 'y':
while input_val('Do you want to play again? (y/n): ', 'Enter either y or n', 'yn').lower() == 'y':
    game_round()
