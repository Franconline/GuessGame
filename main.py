import random

guessesTaken = 0
minNumber = 1
maxNumber = 20

print("Hello! What's your name?: ")
username = input()

number = random.randint(minNumber, maxNumber)

print("Well, " + str(username) + ". I'm thinking in a number between " + str(minNumber) + " and " + str(maxNumber))

# Game's Loop
print("I'm gonna take a guess: ")
while guessesTaken < 6:
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        break
    
    guessesTaken+= 1

if guess == number:
    print("Good Job." + username + ". You did it in " + str(guessesTaken) + ".")
else:
    print("Oh crap. The number was " + str(number))
