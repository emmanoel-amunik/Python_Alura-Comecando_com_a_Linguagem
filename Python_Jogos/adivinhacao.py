print("*" * 29)
print("Welcome to the Guessing game!")
print("*" * 29)

secret_number = 85
user_kick = int(input("Type a number: "))

# user_kick = int(user_kick)  \\ teacher's solution
print("You entered: ", user_kick)


right = user_kick == secret_number
greater = user_kick > secret_number
less = user_kick < secret_number


if right:
    print("You're right!!!")
else:
    if greater:
        print("You're wrong. Your guess was greater than the secret number. ")
    if less:
        print("You're wrong. Your guess was less than the secret number.")


print("*" * 29)
print("End Game")
