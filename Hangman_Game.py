import random
from hangman import word
print("Welcome all to the Hangman Game")
chosen_word=random.choice(word)
print(chosen_word)
game_over=False
correct_letter=[]
lives=6
guess_space=""
for let in chosen_word:
    guess_space+= "_"
print(f"Guess:{guess_space}")
while not game_over:
    guess = input("ask the user to guess a word?\n")
    placeholder = ""
    for letter in chosen_word:
        if guess==letter:
            placeholder+=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            placeholder+=letter
        else :
            placeholder += "_"
    if guess in chosen_word:
        lives+=0
    else:
        lives-=1
        if lives==0:
            game_over=True
            print("Game over")
    if "_" not in placeholder:
        game_over=True
        print("Game Over")
    print(placeholder)
    print(lives)

