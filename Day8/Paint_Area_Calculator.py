#write your code below this line

def paint_calc(height, width, cover):
    numOfCans = round((height * width) / cover)  
    return numOfCans

# write your code above this line
#Define a function called so the code below works.
#Don't change the code below
    
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
result = paint_calc(height=test_h, width = test_w, cover = coverage)
print(f"You'll need {result} cans of paint.")