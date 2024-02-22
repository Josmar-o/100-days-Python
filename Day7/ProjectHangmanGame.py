import random
from HangmanArt import stages
from HangmanArt import logo
from HangmanWords import word_list

i = 0
display = []
lifes = 6
print(logo)

#Selecting the random word
chosen_word = random.choice(word_list)
print(chosen_word)

#Printing the blank spaces
for _ in chosen_word:
        display.append("_")

display_str = "".join(display)
print(display_str)
print(stages[lifes])

#Bucle where is all the logic
while True:
    #These two asignations are for resetting the value everytime
    i = 0
    found = False
    user_letter = input("Guess a letter: ").lower()
    
    #Bucle where all the magic occurs, it iterates the index and compare the letters, also it controls the lifes of the player
    for letter in chosen_word:
        word_letter = chosen_word [i]
        if user_letter == word_letter:
            display[i] = user_letter
            found = True
        i +=1
    if found == False:
         lifes -= 1

    #Printing
    print(stages[lifes])          
    display_str = "".join(display)
    print(display_str)

    #Conditional to exit the program
    if chosen_word == display_str or lifes == 0:
         break
    
print("Thank u for playing this game")


