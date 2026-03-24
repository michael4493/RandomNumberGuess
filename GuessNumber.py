import random

answer = random.randint(1, 100)

attempts = 0

print("Welcome to guess number, a random number between 1 and 100 has generated!")

while True:
    guess = int(input("Make a guess: "))

    attempts += 1

    if guess > answer:
        print("Smaller!")
    elif guess < answer:
        print("Bigger!")
    else:
        print(f"Congratualation! You hit the correct answer! You just made {attempts} attempts!")
        break