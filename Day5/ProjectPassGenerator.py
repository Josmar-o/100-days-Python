import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Select random letters, symbols and numbers using for _ range random.choice and .append
for _ in range(1, nr_letters + 1):
    randomLetter = random.choice(letters)
    password.append(randomLetter)

for _ in range(1, nr_symbols + 1):
    randomSymbol = random.choice(symbols)
    password.append(randomSymbol)

for _ in range(1, nr_numbers + 1):
    randomNumber = random.choice(numbers)
    password.append(randomNumber)

#2nd way of doing the asignation and randomization using functions
    
# #the random.sample(list, number of elements) this will be random and wont be reapeated
# password += random.sample(letters, nr_letters)
# password += random.sample(numbers, nr_numbers)
# password += random.sample(symbols, nr_symbols)


random.shuffle(password)
passwordStr = ''.join(password)
print(f"Your password is {passwordStr}")

    









