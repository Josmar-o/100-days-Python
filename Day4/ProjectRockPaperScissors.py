import random
import sys
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#List for the ASCII ART
hands = [rock, paper, scissors]

#Random number of the computer side
randomNumber = random.randint(0,2)
computerChoose = hands[randomNumber]

#User input
userNumber = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

#Exception handling
if userNumber >= 3 or userNumber <= -1:
    print("Invalid Number")
    #1st way to get out of the program terminating the progress
    #sys.exit()

    #2nd way is just doing a else if everything is ok
else:

    #This is here in case the number the user selected is wrong, so it doesnt affect the program
    userChoose = hands[userNumber]

    #Print of the "hands"
    print(userChoose)
    print("Computer chose:")
    print(computerChoose)

    #If statement selecting who wins
    if userNumber == randomNumber:
        print("It is a draw")
    elif (userNumber == 0 and randomNumber == 2) or \
    (userNumber == 2 and randomNumber == 1) or\
    (userNumber == 1 and randomNumber == 0):
        print("You win")
    else:
        print("You lose")





