#import random and data from game_data
import random
from game_data import data
# from replit import clear
from higherlower_art import logo, vs

SCORE = 0
#randomly pick dictionary from data list of dictionaries
A = random.choice(data)
B = random.choice(data)

#creating function to track score
def score_count():
  return SCORE + 1

#create a function to compare followers
def higher():
  A_follower = A['follower_count']
  B_follower = B['follower_count']
  higher_follower = max(A_follower, B_follower)
  return higher_follower

# def guess_result(guess, comp, against, score):
#   if guess == 'a' and higher() == A['follower_count']:
#     comp = against
#     against = random.choice(data)
#     print(f"You are right, Current score: {score}")
#   elif guess == 'b' and higher() == B['follower_count']:
#     comp = against
#     against = random.choice(data)
#     print(f"You are right, Current score: {score}")
    
guess_again = True

print(logo)
while guess_again:
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
  print(vs)
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
  guess = input("Who has more followers? Type 'A' or 'B': ")
#   clear()
  print(logo)
  if guess == 'a' and higher() == A['follower_count']:
    A = B
    B = random.choice(data)
    SCORE = score_count() 
    print(f"You are right, Current score: {SCORE}")
  elif guess == 'a' and higher() != A['follower_count']:
    guess_again = False
  elif guess == 'b' and higher() == B['follower_count']:
    A = B
    B = random.choice(data)
    SCORE = score_count()
    print(f"You are right, Current score: {SCORE}")
  elif guess == 'b' and higher() != B['follower_count']:
    guess_again = False
    
print(f"Sorry, That's wrong, final score : {SCORE}")