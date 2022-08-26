import random
# # 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(names)

num = len(names)

number = random.randint(0, num - 1)

print(f"{names[number]} is paying.")
# else:
#     print(names[0] + ", you better make your payment")
# if number == 1:
#     payer = names[0]
#     print(f"{payer} is to pay for the meal.")
# else:
#     print(f"{names[1]} is to pay for the meal.")