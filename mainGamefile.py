#import the time modeule
import time

#welcoming the user
name = input("What is your name?")

print ("Hello , " + name, "Time to play Hangman!")

print:" "

#wait for 1 second
time.sleep(1)

print("Start Guessing...")
time.sleep(0.5)

#here we set the secret word
word = "secret"

#create an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

#Create a While loop

#Check if the turns are more than zero

while turns > 0:

    #make a counter that starts with zero
    failed = 0

   #for char in secret_word
    for char in word:

     #to see if the charcter is in the players guess
      if char in guesses:

        #print thrn out the character
        print(char)

    else:

        #if not found, print a dash
        print("_",)

        #and increase the failed counter with one
        failed += 1

        #if failed is equal to zero

        #print you won the game
    if falied == 0:
        print("You Won")

    #exit the file
        break

    print

    #Ask the user go guess a character
    guess = user_input("guess a character:")

    #set the players guess to guesses
    guesses += guess

    #if the word is not found
    if guess not in word:

        #Turn the counter down
        turns -= 1

        #print wrong
        print("Wrong")

        #how many turns
        print("You have", + turns, 'more guesses')

        #if turns reach zero
        if turns == 0:

            #print you lose
            print("You LOSE")

