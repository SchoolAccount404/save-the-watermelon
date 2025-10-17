import random
import string

wordList = ['apple','orange','pear','banana','watermelon']
sliceCounter = 5
guessed = []
hiddenWord = wordList[random.randrange(0,len(wordList))]
winCheck = False
# visibleWord = '_' * len(hiddenWord)

print(hiddenWord)
print('_' * len(hiddenWord))


while sliceCounter > 0: # or not '_' in visibleWord:
    # print(visibleWord)
    guess = input('Enter your guess: ').lower()
    if guess not in string.ascii_letters or len(guess) != 1:
        print('Invalid input')
        continue

    if guess in hiddenWord:
        if guess not in guessed:
            print('Good guess!')
            guessed.append(guess)
            # for i in range(0,len(hiddenWord)):
            #     if hiddenWord[i] in guessed:
            #         visibleWord[i] = guess
        else:
            print('You already guessed', guess, 'and it was correct.')
    elif guess not in guessed:
        print('Incorrect guess.')
        guessed.append(guess)
        sliceCounter -= 1
    else:
        print('You already guessed', guess, 'and it was incorrect.')

    print('Slices Remaining:', sliceCounter)

    if sliceCounter <= 0:
        print('You Lost, the word was', hiddenWord)
        break

    winCheck = True
    for char in hiddenWord:
        if char in guessed:
            print(char,end='')
        else:
            winCheck = False
            print('_',end='')
    print()
    if winCheck:
        print("You Win!")
        break
