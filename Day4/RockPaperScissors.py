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
hands = [rock, paper, scissors]
randomNumber = random.randint(0,2)
computerChoose = hands[randomNumber]

userNumber = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if userNumber >= 3 or userNumber <= -1:
    print("Invalid Number")
    #sys.exit()
else:
    userChoose = hands[userNumber]
    print(userChoose)
    print("Computer chose:")
    print(computerChoose)

    if userChoose == computerChoose:
        print("It is a draw")
    elif (userChoose == 0 and computerChoose == 2) or \
    (userChoose == 2 and computerChoose == 1) or\
    (userChoose == 1 and computerChoose == 0):
        print("You win")
    else:
        print("You lose")





