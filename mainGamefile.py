# import the time modeule
import time

# importing the random module
import random

# list of words
words = ["ice", "strawberry", "heaven", "paris", "exodus", "circus", "devilish", "divine", "ultimatum"]

# Save underscore for easier use
underScore = "_ "

# amount of words
y = 0
for x in words:
    y = y + 1

# welcoming the user
name = input("What is your name?")

print("Hello, " + name + " time to play Hangman!")

# wait for 1 second
time.sleep(1)

print("Start Guessing...")
time.sleep(0.5)

# here we set the secret word
word = words[random.randint(0,y-1)]

print (word)
# create an variable with an empty value
guesses = ''

# determine the number of turns
turns = 10

# Create a While loop

# Check if the turns are more than zero

while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # Variable to store user's progress
    progress = ""

    # for char in secret_word
    for char in word:

        # to see if the charcter is in the players guess
        if char in guesses:

            # print thrn out the character
            progress += char

        else:

            # if not found, print a dash
            progress += underScore

            # and increase the failed counter with one
            failed += 1

            # if failed is equal to zero

    # print you won the game
    if failed == 0:
        print("You Won " +str(10-turns)+ " wrong guesses.")

    # exit the file
        break

    print(progress)
    print("")
    # Ask the user go guess a character
    guess = input("Guess a character:")

    # set the players guess to guesses
    guesses += guess

    # if the word is not found
    if guess not in word:

        # Turn the counter down
        turns -= 1

        # print wrong
        print("Wrong")

        # how many turns
        print("You have", + turns, 'more guesses')
        print(word)
        # if turns reach zero
        if turns == 0:

            # print you lose
            print("You LOSE")

