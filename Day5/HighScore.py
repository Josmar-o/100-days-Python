student_scores = [1, 50, 100, 40]
grade = 0
for score in student_scores:
  if grade < score:
    grade = score

print(f"The highest score in the class is: {grade}")