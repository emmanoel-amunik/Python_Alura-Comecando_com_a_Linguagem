import random


print("*" * 29)
print("Welcome to the Guessing game!")
print("*" * 29)


for attempts in range(3):

    secret_number = random.randrange(1, 101)

    print(f"Attempt {attempts+1} of 3")
    user_kick = int(input("Type a number: "))

    if user_kick < 1 or user_kick > 100:
        print("You need to enter a number between 1 and 100")
        continue

    right = user_kick == secret_number
    greater = user_kick > secret_number
    less = user_kick < secret_number

    print("You entered: ", user_kick)

    if right:
        print("You're right!!!")
        break
    else:
        if greater:
            print("You're wrong. Your guess was greater than the secret number. ")
        if less:
            print("You're wrong. Your guess was less than the secret number.")
    print("*" * 15)


print("End Game")
