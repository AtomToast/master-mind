#!/usr/bin/python3

from random import randint

code = []

for x in range(0, 4):
    code.append(randint(1, 6))

print("There is a hidden code of 4 digits(1-6). Try to guess it!\nI will tell you how many digits you got right. You need to solve the code in 12 tries or you lose!")

attempts_left = 12

while attempts_left > 0:
    print(f"{attempts_left} attempts remaining")
    guess = input("Enter your guess: ")

    try:
        guess_list = [int(i) for i in guess]
    except ValueError:
        print("Please enter a valid 4 digit code!")
        continue

    if len(guess_list) != 4:
        print("Please enter a valid 4 digit code!")
        continue

    correct_guesses = 0

    for i, v in enumerate(guess):
        if code[i] == int(v):
            correct_guesses += 1

    if correct_guesses == 4:
        print(f"You guessed the code with {attempts_left} attempts left")
        break

    print(f"You guessed {correct_guesses} digits correctly!")
    attempts_left -= 1

print(f"Oops! You're out of attempts! The correct code was {code}")
