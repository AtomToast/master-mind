#!/usr/bin/python3

from random import randint


def generate_code():
    code = []

    for x in range(0, 4):
        code.append(randint(1, 6))

    return code


def generate_solutions():
    possible_solutions = []
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    possible_solutions.append([i, j, k, l])

    return possible_solutions


def make_guess(possible_solutions):
    guess_index = randint(0, len(possible_solutions)-1)
    guess = possible_solutions.pop(guess_index)
    print(guess)
    return guess


def evaluate_guess(code, guess):
    correct_guesses = 0
    wrong_position = 0
    for i, v in enumerate(guess):
        if code[i] == v:
            correct_guesses += 1
        elif v in code:
            wrong_position += 1

    return correct_guesses, wrong_position


# help
def evaluate_guess_results(previous_guesses, possible_solutions):
    new_possible_solutions = []
    for s in possible_solutions:
        for g in previous_guesses:
            correct_guesses, wrong_position = evaluate_guess(
                previous_guesses[-1]["guess"], s)
            if correct_guesses < g["correct_guesses"] and wrong_position < g["wrong_position"]:
                break
        else:
            new_possible_solutions.append(s)

    return new_possible_solutions


def main():
    code = generate_code()
    possible_solutions = generate_solutions()
    attempts_left = 24
    previous_guesses = []

    while attempts_left > 0:
        print("possible solutions: ", len(possible_solutions))
        guess = make_guess(possible_solutions)

        correct_guesses = 0
        wrong_position = 0

        correct_guesses, wrong_position = evaluate_guess(code, guess)

        if correct_guesses == 4:
            print(f"You guessed the code with {attempts_left} attempts left!")
            exit()

        print(f"{correct_guesses} correct, {wrong_position} wrong position")
        previous_guesses.append(
            {"correct_guesses": correct_guesses, "wrong_position": wrong_position, "guess": guess})
        possible_solutions = evaluate_guess_results(
            previous_guesses, possible_solutions)

        attempts_left -= 1

    print(f"Oops! You're out of attempts! The correct code was {code}")
    print("possible solutions: ", len(possible_solutions))


if __name__ == "__main__":
    main()
