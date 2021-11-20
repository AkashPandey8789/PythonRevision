import random

a = 1
b = 3.53
c = 6j

print(type(a))
print(type(b))
print(type(c))

userInput = input("Guess the number:")
randomNumber = random.randint(0, 9)
while int(userInput) != randomNumber:
    if int(userInput) < randomNumber:
        print("Think something bigger than this!!")
    elif int(userInput) > randomNumber:
        print("Think something small!!")
    userInput = input("Guess the number:")

print("Guessed it!! ", randomNumber)
