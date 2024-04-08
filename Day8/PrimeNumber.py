# write your code below this line

def isPrime (number):
#       is_prime = True
#   for i in range(2, number):
#     if number % i == 0:
#       is_prime = False
#   if is_prime:
#     print("It's a prime number.")
#   else: 
#     print("It's not a prime number.")  
    numbers = []
    for i in range(1, number + 1):
        if number % i == 0:
            numbers.append(i)

    if len(numbers) ==2:
        return("It's a prime number.")
    else:
        return("It's not a prime number.")

# write your code above this line
# change any of the code below
n = int(input()) # Check this nunber

print(isPrime(n))