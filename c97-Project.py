import random
number = random.randint(1, 9)
chance = 0
print("Number Guessing Game")
while chance < 5:
    print("Guess a number between 1 and 9")
    if (chance == 0):
        guess = int(input("Enter your guess: "))
        if (guess == number):
            print("Congrats, you won!!!")
            chance = 5
        else:
            chance = chance + 1
            if (guess > number):
                print("Your guess was too high: Guess a number lower than ", guess)
            else:
                print("Your guess was too low: Guess a number higher than ", guess)
    elif (chance == 1):
        guess = int(input("Enter your guess: "))
        if (guess == number):
            print("Congrats, you won!!!")
            chance = 5
        else:
            chance = chance + 1
            if (guess > number):
                print("Your guess was too high: Guess a number lower than ", guess)
            else:
                print("Your guess was too low: Guess a number higher than ", guess)
    elif (chance == 2):
        guess = int(input("Enter your guess: "))
        if (guess == number):
            print("Congrats, you won!!!")
            chance = 5
        else:
            chance = chance + 1
            if (guess > number):
                print("Your guess was too high: Guess a number lower than ", guess)
            else:
                print("Your guess was too low: Guess a number higher than ", guess)
    elif (chance == 3):
        guess = int(input("Enter your guess: "))
        if (guess == number):
            print("Congrats, you won!!!")
            chance = 5
        else:
            chance = chance + 1
            if (guess > number):
                print("Your guess was too high: Guess a number lower than ", guess)
            else:
                print("Your guess was too low: Guess a number higher than ", guess)
    elif (chance == 4):
        guess = int(input("Enter your guess: "))
        if (guess == number):
            print("Congrats, you won!!!")
            chance = 5
        else:
            chance = chance + 1
            print("Sorry, you lost. The number is ", number)