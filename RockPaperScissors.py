import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to the game 'Rock', 'Paper', 'Scissors'!!!")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
comp_choice = random.randint(0,2)

# comp_choice = 1
if choice >= 3 or choice < 0:
    print("You entered and invalid number, you lose!")
elif comp_choice == 0 and  choice == 1:
    comp_choice = rock
    choice = paper
    print(f"{choice}\n computer chose: {comp_choice}\n You win")

elif comp_choice == 1 and choice == 0:
    comp_choice = paper
    choice = rock
    print(f"{choice}\n computer chose: {comp_choice}\n You lose")

elif comp_choice == 2 and choice == 0:
    comp_choice = scissors
    choice = rock
    print(f"{choice}\n computer chose: {comp_choice}\n You win")

elif comp_choice == 0 and choice == 2:
    comp_choice = rock
    choice = scissors
    print(f"{choice}\n computer chose: {comp_choice}\n You win")

elif comp_choice == 1 and choice == 2:
    comp_choice = paper
    choice = scissors
    print(f"{choice}\n computer chose: {comp_choice}\n You win")

elif comp_choice == 2 and choice == 1:
    comp_choice = scissors
    choice = paper
    print(f"{choice}\n computer chose: {comp_choice}\n You lose")

elif comp_choice == choice:
    print(f"{choice}\n computer chose: {comp_choice}\n It's draw")

