import random

digits = []
for i in range(9):
    digits.append(str(i + 1))

secret_num = ""
for i in range(4):
    secret_num += digits.pop(random.randrange(0, len(digits)))

guess = ""
n_of_guesses = 0
while guess != secret_num:
    guess = input("Enter guess: ")
    if len(guess) != 4:
        print("Guess must be four digits")
        continue
    
    bulls = 0
    cows = 0
    n_of_guesses += 1
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            bulls += 1
        elif guess[i] in secret_num:
            cows += 1

    print(bulls, "bulls and", cows, "cows")

print("You got it in", n_of_guesses, "tries!")
