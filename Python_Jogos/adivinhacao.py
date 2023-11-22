print("*****************************")
print("Welcome to the Guessing game!")
print("*****************************")

secret_number = 42
user_kick = int(input("Type a number: "))

print("You entered: ", user_kick)

# user_kick = int(user_kick)  \\ teacher's solution
if secret_number == user_kick:
    print("You're right!!!")
else:
    print("You're wrong. Try again!")
