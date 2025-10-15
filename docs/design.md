## Problem statement & target audience (2--3 sentences).


## Game rules & win/lose conditions.
You are presented with a random word, with most of the letters being unknown to you.
You must guess

## Core features (must-have) vs stretch goals (nice-to-have).


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
the original word is just stored as a string outside of the loop

remaining slices just stored as integer outside of the loop


## Module/function responsibilities.
