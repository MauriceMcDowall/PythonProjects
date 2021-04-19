## Number Guessing
# * Program in which the computer randomly chooses a number
# * The user is given a hint on what range the number lies between
# * Each time the user guesses the number wrong, they get another hint in a smaller range, but their score gets reduced
# * Will need functions to compuare the inputed number with the guessed number
# * To compute the difference between the two
# * And to check whether an actual number was inputed or not.

#---Generating a random number---#
import random
RandomNum = (random.randint(0,9))
Score = 0.0


# Creating a function to ask the user if they want to generate a random number
def UserSelection():
    print("Would you like to generate a random number?")
    UserSelect = input("")

    if UserSelect == 'y':
        print("*---Generating A Random Number---*")


# Creating a function to print hints to the user
def hint():
    if RandomNum >= 1 and RandomNum <= 3:
        print("Random Number Is More Than 1, But Less Than 3")

    elif RandomNum >= 4 and RandomNum <= 7:
        print("Random Number Is More Than 4, But Less Than 7")

    elif RandomNum >= 8 and RandomNum <= 10:
        print("Random Number Is More Than 8, But Less Than 10")




# Creating a function which takes the users input and compares it against the random number 
def UserInput():
    print("Enter your guess")
    UserGuess = input()
    
    while UserGuess != RandomNum:
       print("You are WRONG! Try Again")
       UserSelection()
       hint()
       UserInput()

    if UserGuess == RandomNum:
        print("Well Done")

# Calling each function
UserSelection()
hint()
UserInput()
