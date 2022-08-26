# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
count = 0
for i in student_heights:
  count = count + 1
total = 0
for i in student_heights:
  total = total + i
final_sum = round(total / count)
print(final_sum)
    





# for i in student_heights[n]:
#     student_heights[n] += 1
#     print(student_heights[n])
