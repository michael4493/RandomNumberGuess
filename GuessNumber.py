import random


a = int(input("Input the minimum of the number: "))
b = int(input("Input the maximum of the number: "))
answer = random.randint(a, b)
attempt = 0


while True:
    guess = int(input("Input your guess number: "))
    attempt += 1
    if guess > answer:
        print("Smaller!")
    elif guess < answer:
        print("Bigger!")
    else:
        print("You hit the correct number!")
        print(f"You just made {attempt} guesses to hit the answer!")
        break