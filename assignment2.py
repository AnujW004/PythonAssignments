import random
number = random.randint(1, 100)
guess = None
print("Guess a number between 1 and 100:")
while guess != number:
    try:
        guess = int(input())
        if guess > number:
            print("Too high! Try again:")
        elif guess < number:
            print("Too low! Try again:")
        else:
            print("Congratulations! You guessed the number.")
    except ValueError:
        print("Please enter a valid number.")

