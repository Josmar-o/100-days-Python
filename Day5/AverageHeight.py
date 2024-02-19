student_heights = [158, 190, 170, 174]

sum = 0
i =0

for heights in student_heights:
  sum += heights
  i+=1

result = round(sum/i)

print(f"total height = {sum}")
print(f"number of students = {i}")
print(f"average height = {result}")