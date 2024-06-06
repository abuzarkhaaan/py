import random

num = random.randint(1,5)
guess = int(input("Please enter a number to guess the number"))

while guess != num:
    if guess < num:
        print("your guess is too low")
    elif guess > num:
        print("your guess is too high")
    guess = int(input("guess again"))
print("you guessed right")

