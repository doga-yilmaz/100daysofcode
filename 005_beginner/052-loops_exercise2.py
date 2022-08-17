student_scores = input("What is the scores").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

x = 0
for score in student_scores:
    if x < score:
        x = score
print(f"The highest score in the class: {x}")

y = 100
for score in student_scores:
    if y > score:
        y = score
print(f"The lowest score in the class: {y}")

# She did'not want the lowest score, bu it's fine :)