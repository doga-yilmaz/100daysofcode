student_heights = input("Input a list of student heights ").split()


for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  #print(student_heights[n])

x = 0
for i in student_heights:
    x += i
print (f"Sum of heights is {x} ")

y = 0
for n in student_heights:
    y += 1
print(f"Number of student is {y}")

print ("Average height is ", round(x / y))
