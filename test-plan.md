Test matrix (valid/invalid inputs, repeated guesses, win/lose edges)

input_val covers all the input stuff, bad inputs just make it ask for another input until you give a valid one

I've tried multiple letters where there should be one, or one where there should be multiple

I've tried things like 'ab' as input with incheck being ascii_letters, to see if the length checker was necessary, which it was,
 and I've tried things like 'f' or 'uit' when incheck was the category names, and it didn't see them as valid input because they didn't match up properly

as far as I have tested, input_val can handle it all

the guesser function has the repeat guesses thing covered, and I'm pretty sure there aren't even any edge cases with wins or losses

## test transcript
note: user inputs in the category selection process have been isolated from printed text for clarity
```
Select a category:
fruits
test

fr

Invalid input
Select a category:
fruits
test

f

Invalid input
Select a category:
fruits
test

fruits

_____l_u__
Enter your guess: c
Good guess!
Slices Remaining: 5
c____l_u__
Enter your guess: c
You already guessed c and it was correct.
Slices Remaining: 5
c____l_u__
Enter your guess: c
You already guessed c and it was correct.
Slices Remaining: 5
c____l_u__
Enter your guess: a
Good guess!
Slices Remaining: 5
ca__al_u__
Enter your guess: z
Incorrect guess.
Slices Remaining: 4
ca__al_u__
Enter your guess: y
Incorrect guess.
Slices Remaining: 3
ca__al_u__
Enter your guess: y
You already guessed y and it was incorrect.
Slices Remaining: 3
ca__al_u__
Enter your guess: n
Good guess!
Slices Remaining: 3
can_al_u__
Enter your guess: t
Good guess!
Slices Remaining: 3
cantal_u__
Enter your guess: 
Your guess must be a single letter.
Enter your guess: o
Good guess!
Slices Remaining: 3
cantalou__
Enter your guess: p
Good guess!
Slices Remaining: 3
cantaloup_
Enter your guess: e
Good guess!
Slices Remaining: 3
cantaloupe
You Win!
Do you want to play again? (y/n): y
Select a category:
fruits
test

test

_olo_
Enter your guess: z
Incorrect guess.
Slices Remaining: 4
_olo_
Enter your guess: x
Incorrect guess.
Slices Remaining: 3
_olo_
Enter your guess: y
Incorrect guess.
Slices Remaining: 2
_olo_
Enter your guess: v
Incorrect guess.
Slices Remaining: 1
_olo_
Enter your guess: m
Incorrect guess.
Slices Remaining: 0
You Lost, the word was dolor
Do you want to play again? (y/n): n
```
transcript 2 because I forgot to show testing multiple letters in the playing part
```
Select a category:
fruits
test

fruits

_a__a_o___
Enter your guess: ab
Your guess must be a single letter.
Enter your guess: ab
Your guess must be a single letter.
Enter your guess: ca
Your guess must be a single letter.
Enter your guess: c
Good guess!
Slices Remaining: 5
ca__a_o___
Enter your guess: n
Good guess!
Slices Remaining: 5
can_a_o___
Enter your guess: t
Good guess!
Slices Remaining: 5
canta_o___
Enter your guess: l
Good guess!
Slices Remaining: 5
cantalo___
Enter your guess: u
Good guess!
Slices Remaining: 5
cantalou__
Enter your guess: p
Good guess!
Slices Remaining: 5
cantaloup_
Enter your guess: e
Good guess!
Slices Remaining: 5
cantaloupe
You Win!
Do you want to play again? (y/n): n
```
and another to test inputting numbers
```
Select a category:
fruits
test

fruits

m__g_
Enter your guess: 6
Your guess must be a single letter.
Enter your guess: 5
Your guess must be a single letter.
Enter your guess: a
Good guess!
Slices Remaining: 5
ma_g_
Enter your guess: n
Good guess!
Slices Remaining: 5
mang_
Enter your guess: o
Good guess!
Slices Remaining: 5
mango
You Win!
Do you want to play again? (y/n): n
```