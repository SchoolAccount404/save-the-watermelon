## Problem statement & target audience (2--3 sentences).
To create a word guessing game for all ages. Users will guess characters to try and guess the hidden word.

## Game rules & win/lose conditions.
You are presented with a random word, with most of the letters being unknown to you.
You must guess

## Core features (must-have) vs stretch goals (nice-to-have).
Core Features:
* Randomly select a secret word from a list.
* Show a masked version (e.g., ```_ a _ e```).
* Player guesses letters; correct guesses reveal letters.
* Incorrect guesses reduce "slices" (lives). If slices reach 0, the watermelon is "sliced" and the player loses.
* Win when all letters are revealed before slices run out.
Stretch Goals:
* ASCII art stages
* difficulty levels
* hint
* word categories
* scoreboard

## Basic flow diagram or bullet-flow (start → loop guess → win/lose).
start

set slice timer to something

get random word from list

make string of same length as word, but all underscores

reveal 1 or 2 letters, as if player had correctly guessed

player can now see underscored version and begin guessing

loop

player guesses one letter

if the letter is correct, 
```
slice timer: 5
guess: w
word (hidden): "wordword"
                v   v
word (shown):  "________"
word (shown):  "w___w___"
slice timer: 5
```
if the letter is incorrect,
```
slice timer: 5
guess: a
word (hidden): "wordword"
word (shown):  "________"
prints that you got it wrong
slice timer: 4
```
if given user input is invalid (ie. number, symbol, multiple characters), it simply tells the user, continuing the loop without having changed any variables

then checks,

if slice timer is 0, game over

if no more underscores remaining/ all correct letters guessed, you win

otherwise, the loop continues

## Data design: How you store the word, revealed letters, guessed letters, remaining slices
the word is just stored as a string before the loop

revealed/guessed letters are strings stored in a list before the loop

remaining slices just stored as integer before the loop


## Module/function responsibilities.
game.py - just the access point

logic.py
* input_val(prompt, errortext, conditions...)
  * Used in place of input(), runs until given an input that fits the given conditions, giving the errortext when forced to repeat 
* guesser
  * asks user to guess, and then processes what should happen as a result
  * can modify the list [] of guessed characters directly, but not the integer slice variable, and so returns that
  * needs to be able to do a random correct guess
* game_round
  * sets up variables (word list, guessed letters, slices, a random word from that list)
  * gets one or two random correct guesses, and then shows the user the word, with unguessed letters replaced with underscores
  * begins loop, where it asks for a guess, shows slices remaining, and the known word as above, giving the player victory if it prints no underscores, or a loss if they run out of slices
* replayability_function
  * just runs game_round, and then asks if you want to again, until you say no

words.py
* list_picker
  * stores the different word lists/categories, and has you pick one, which it will then return










