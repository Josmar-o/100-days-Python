line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

# if position[0] == "A" and position[1] == "1":
#   line1[0] = "X"
# elif position[0] == "A" and position[1] == "2":
#   line2[0] = "X"
# elif position[0] == "A" and position[1] == "3":
#   line3[0] = "X"
# elif position[0] == "B" and position[1] == "1":
#   line1[1] = "X"
# elif position[0] == "B" and position[1] == "2":
#   line2[1] = "X"
# elif position[0] == "B" and position[1] == "3":
#   line3[1] = "X"
# elif position[0] == "C" and position[1] == "1":
#   line1[2] = "X"
# elif position[0] == "C" and position[1] == "2":
#   line2[2] = "X"
# elif position[0] == "C" and position[1] == "3":
#   line3[2] = "X"

letter = position[0]
ABC = ["A", "B", "C"]
letterIndex = ABC.index(letter)
numberIndex = int(position[1]) - 1
map[numberIndex] [letterIndex] = "X"
    

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")