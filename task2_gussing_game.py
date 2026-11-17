
import random

print("NUMBER GUESSING GAME")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

number = random.randint(start, end)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")

    elif guess > number:
        print("Too high! Try again.")

    else:
        print("Congratulations! Correct guess!")
        print("Total attempts:", attempts)
        break
