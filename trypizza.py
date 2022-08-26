# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Pizza prices
L = 25
M = 20
S = 15
#Pepperoni
Pep_for_s = 2
Pep_for_m = 3
Pep_for_l = 3
#Cheese
extra_c = 1

if size == "L":
    Lbill = 25
    if add_pepperoni == "Y":
        add_Pep = Lbill + Pep_for_l
        if extra_cheese == "Y":
            add_Pep = Lbill + Pep_for_l + extra_c
            print(f"Your final bill is: ${add_Pep}")
        else:
            print(f"Your final bill is: ${add_Pep}")
    elif extra_cheese == "Y":
        Lbill += extra_c
        print(f"Your final bill is: ${Lbill}.")
else:
    print("InProgress")