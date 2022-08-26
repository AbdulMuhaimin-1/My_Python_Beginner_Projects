import random
from art import logo

computer_guess = random.randint(2, 99)

print(logo)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 - 100.")
# print("Spoiler:",computer_guess)
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == 'easy':
    ATTEMPT = 10
else:
    ATTEMPT = 5

def wrong_guess():
    return ATTEMPT - 1

def compare(user_guess, computer_guess):
    if user_guess > computer_guess:
        return "Too high."
    elif user_guess < computer_guess:
        return "Too Low."
    elif user_guess == computer_guess:
        return f"You got it!, the answer was {computer_guess}"

guess_again = True
while guess_again:
    print(f"You have {ATTEMPT} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess != computer_guess:
        ATTEMPT = wrong_guess()
        if ATTEMPT == 0:
            print(compare(user_guess, computer_guess))
            print("You've run out of attempts, you lose!.")
            guess_again = False
        else:
            print(compare(user_guess, computer_guess))
            print("Guess Again")
    else:
        print(compare(user_guess, computer_guess))
        guess_again = False

#TODO1: Print a welcom note and create a variable that takes the difficulty level 'easy' or 'hard'.
#TODO2: Create an 'if' statement that depending on what player chooses from 'TODO1' assign attempts to variable ATTEMPT, 10 for 'easy' and
#5 for 'hard'. Print a statement based on the difficulty telling the player the number of attempt they have before starting the game.
#TODO3: Depending on what player chooses create a wrong_guess() function that returns the ATTEMPT, reducing it by 1.
#TODO4: I need to write a code to show the player the number of attempts remaining before guessing a number.
#TODO5: If a player guesses a number, i will need a function called compare() to compare the number with the computer's guess.
#TODO6: An if statement to check if attempt = 0 then the game ends else call  compare
#TODO7: If the attempts is not equal to '0',then the player should have a chance to guess the correct answer, so the player should be taken back where they can guess again.