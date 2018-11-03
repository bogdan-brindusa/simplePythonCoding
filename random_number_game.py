# A simple game using 'while' loop and a function from module 'random'

import random

number = random.randint(1, 100)

# user is prompted to choose a number in a range
print("Guess a magic number between 1 and 100")

# 'while' loop will finish when user guess the number
guess = -1
while guess != number:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Yes, the number is ", number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
