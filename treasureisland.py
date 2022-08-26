print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

treasure_hunt = input("The treasure is quiet far from you now.\nWhere do you want to heard towards, Left, Right or Foward?\n")


if treasure_hunt.lower() == "left":
    cave = input('There\'s a cave in front,\nDo you want to go in or take the road on your right, "Enter" Or "Right"?\n')
    if cave.lower() == "right":
        river = input("There is a river infront of you.\nDo you want swim across or you wait for a boat, Swim Or Wait?\n")
        if river.lower() == "wait":
            shiny_thing = input("In the middle somewhere in the river,\nyou see a faint shiny object down in the  river, Dive Or Go?\n")
            if shiny_thing.lower() == "dive":
                door = input("There are two door beneath the river infront of you,\nWhich of them are you entering, the doors are of two colors, Blue Or White?\n")
                if door.lower() == "blue":
                    print("You Win!!!")
                elif door.lower() == "red":
                    print("Ooooh! GameOver!! You just turned to fried fish!.")
                else:
                    print("Oooh!!! GameOver!! You where almost there!")
            else:
                print("GameOver!!!\nYou were attacked by Scavengers at the riverbank!")
        else:
            print("GameOver!!!, You were eaten by a Shack!.")
    else:
        print("You went in?!!!\nThat is a Lion's, you have become lunch..GameOver!!! ")
else:
    print("You fell into a hole or You are lost..GameOver!!!")