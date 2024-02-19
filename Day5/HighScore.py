student_scores = [91, 94, 80, 99]
grade = 0
for score in student_scores:
  if grade < score:
    grade = score

print(f"The highest score in the class is: {grade}")