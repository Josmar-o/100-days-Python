import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

people = (len(names)-1)

randomInt = random.randint(0, people)

print(names[randomInt] + " is going to buy the meal today!")
