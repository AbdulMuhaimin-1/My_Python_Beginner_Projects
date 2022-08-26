# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num1 = name1 + name2

result = num1.lower()

true1 = result.count("t")
true2 = result.count("r")
true3 = result.count("u")
true4 = result.count("e")

add_true = true1 + true2 + true3 + true4

love1 = result.count("l")
love2 = result.count("o")
love3 = result.count("v")
love4 = result.count("e")

add_love = love1 + love2 + love3 + love4

score = str(add_true) + str(add_love)

Love_score = int(score)

if (Love_score < 10) or (Love_score > 90):
    print(f"Your score is {Love_score}, you go together like coke and mentos.")

elif (Love_score >= 40)  and (Love_score <= 50):
    print(f"Your score is {Love_score}, you are alright together")

else:
    print(f"Your score is {Love_score}.")

