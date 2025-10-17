```
FUNCTION input_val(prompt='Error, no prompt given', failtext='Invalid input', incheck=ascii_letters, uselen=True):
    userInput = input(prompt).lower()
    WHILE userInput NOT IN incheck OR (uselen and len(userInput) != 1)
        DISPLAY failtext
        userInput = input(prompt).lower()
    RETURN userInput
    
FUNCTION pick_category
    catDict = {'fruits': ['apple', 'orange', 'pear', 'banana', 'watermelon', 'cantaloupe', 'cherry', 'durian', 'mango', 'peach', 'pomegranate'],
                'test': ['lorem', 'ipsum', 'dolor']}
    chosenCat = input_val('Select a category:\n' + '\n'.join(list(catDict.keys())) + '\n', 'Invalid input',catDict.keys(), False)
    RETURN catDict[chosenCat]

FUNCTION guesser(hiddenWord, guessed, sliceCounter, randGuess=False):
    IF NOT randGuess THEN
        guess = input_val('Enter your guess: ', 'Your guess must be a single letter.')
    ELSE
        guess = hiddenWord[randomized]
        WHILE guess IN guessed
            guess = hiddenWord[randomized]

    IF guess IN hiddenWord THEN
        IF guess NOT IN guessed THEN
            IF NOT randGuess THEN
                DISPLAY 'Good guess!'
            guessed.append(guess)
        ELIF NOT randGuess THEN
            DISPLAY 'You already guessed' + guess + 'and it was correct.'

    ELIF guess NOT IN guessed THEN
        IF NOT randGuess THEN
            DISPLAY 'Incorrect guess.'
        guessed.append(guess)
        sliceCounter -= 1
    ELIF NOT randGuess THEN
        DISPLAY 'You already guessed' + guess + 'and it was incorrect.'

    RETURN sliceCounter

FUNCTION game_round
    category = pick_category()
    sliceCounter = undecided_int
    guessed = ∅
    hiddenWord = category[randomized]

    CALL guesser(hiddenWord, guessed, sliceCounter, randGuess=True)
    CALL guesser(hiddenWord, guessed, sliceCounter, randGuess=True)

    FOR char IN hiddenWord
        IF char IN guessed THEN
            DISPLAY char, no newline
        ELSE
            DISPLAY "_", no newline
    DISPLAY newline

    WHILE sliceCounter > 0
        sliceCounter = CALL guesser(hiddenWord, guessed, sliceCounter)

        DISPLAY "Slices Remaining: " + sliceCounter

        IF sliceCounter <= 0
            DISPLAY "You Lost, the word was " + hiddenWord
            BREAKWHILE

        winCheck = True
        FOR char IN hiddenWord
            IF char IN guessed THEN
                DISPLAY char, no newline
            ELSE
                winCheck = False
                DISPLAY "_", no newline
        DISPLAY newline
        IF winCheck
            DISPLAY "You Win!"
            BREAKWHILE
            
FUNCTION run_round
    game_round()
    WHILE input_val('Do you want to play again? (y/n): ', 'Enter either y or n', 'yn').lower() == 'y':
        game_round()
```