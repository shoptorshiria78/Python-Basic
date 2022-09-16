import random
secretNumber = random.randint(1,10)
print('I am thinking of a number between 1 and 5')


#ask player to guess
for guessesTaken in range(1,4):
    print("take a guess.")
    guess = int(input())


    if guess < secretNumber:
        print ("Your guess is too low")

    elif guess > secretNumber:
        print("Your guess is too high")

    else:
        break


if guess == secretNumber:
        print(" You are the ultimate winner !!!!!")
        print("Good job! you guessed secret number in " + str(guessesTaken) + " " + "Guesses!")

else:
        print(" Nope !! the number computer was thinking was " + str(secretNumber))

