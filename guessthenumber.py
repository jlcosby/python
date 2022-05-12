import random

guesses = 0

number = random.randint(1,100)
print("Guess a number between 1-100")

while guesses < 5:
    print("Take a guess.")
    guess = input()
    guess = int(guess)
    
    guesses = guesses + 1

    if guess < number:
        print("Too low!")

    if guess > number:
        print("Too high!")

    if guess == number:
        break

if guess == number:
    guesses = str(guesses)
    print("You must be a mindreader!")

if guess != number:
    number = str(number)
    print("Wrong! My number was " + number)