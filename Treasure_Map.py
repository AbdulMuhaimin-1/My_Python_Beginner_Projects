# π¨ Don't change the code below π
row1 = ["βΊοΈ","b","c"]
row2 = ["1","2","3"]
row3 = ["i","ii","iii"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# π¨ Don't change the code above π

#Write your code below this row π

horizontal = int(position[0])
vertical = int(position[1])
hori = horizontal - 1
vert = vertical -1
map[vert][hori] = "X"


# map[vert][hori] = "X"

# print(row1)
# if vert == 0:
#     map[vert][hori] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# elif vert == 1:
#      row2[hori] = "X"
#      print(f"{row1}\n{row2}\n{row3}")
# else:
#     row3[hori] = "X"
#     print(f"{row1}\n{row2}\n{row3}")







#Write your code above this row π

# π¨ Don't change the code below π
print(f"{row1}\n{row2}\n{row3}")