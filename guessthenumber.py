guess = int(input("What whole number between 1-100 am I thinking of? "))

if guess == 28:
    print("You are a mind reader!! ")
elif guess >= 25 and guess <=27:
    print("Guess a little higher! ")
elif guess <= 24 and guess >= 1:
    print("Guess higher! ")
elif guess >= 29 and guess <= 34:
    print("Guess a little lower! ")
elif guess <= 100 and guess >= 35:
    print("Guess lower! ")
else:
    print("That's not a number between 1-100! ")