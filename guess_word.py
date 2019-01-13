import random


def user_input():
    while True:
        inp = input("enter your guess: ")
        if not inp.isnumeric():
            break
        else:
            print("wrong input ! please enter only letters")
    return inp


guesses = []

with open("guesses.txt", "r") as guess:
    for each in guess:
        guesses.append(each.strip("\n"))

guess_phrase = random.choice(guesses)
input_values = ""
i = 0
indexes = []
canvas = []
correct_counter = 0
wrong_attempts = 0
wrong_words = []
wrong = ""
counter = (len(guess_phrase) - 1)
for each in guess_phrase:
    canvas.append("-")
while True:
    if counter < 0:
        break
    current_counter = correct_counter
    print("current state : ", " ".join(canvas))
    user_guess = user_input()
    for index, value in enumerate(guess_phrase):
        if value.lower() == user_guess.lower():
            # input_values += user_guess
            canvas[index] = user_guess
            correct_counter += 1
        else:
            if user_guess not in guess_phrase:
                wrong = user_guess
    wrong_words.append(wrong)

    if correct_counter == current_counter:
        counter -= 1
        wrong_attempts += 1
        print(f"wrong ! wrong attempts : {wrong_attempts} / {len(guess_phrase)}")
        print(f"wrong words : ", " , ".join(wrong_words))
        if wrong_attempts == len(guess_phrase):
            print("you lost")
    if "-" not in canvas:
        print(" ".join(canvas))
        print("you won")
        break
