import random

num = random.randint(1, 10)
guess =None

while guess != num:
    guess = input("Enter a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! That's the selected number!")
        break
    else:
        print("nope, sorry. try again!")