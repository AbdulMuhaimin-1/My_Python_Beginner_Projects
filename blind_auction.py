# from replit import clear
# clear()
#HINT: You can call clear() to clear the output in the console.
# from art import logo
# print(logo)

bid_higher = {}
other_bidders = True

def find_highest(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        # winner = bidder
  print(f"The winner is {bidder} with a bid of Ghc{highest_bid}")
  
while other_bidders:
  name = input("What is you name?: ").lower()
  bid = int(input("What's your bid?: Ghc"))
  bid_higher[name] = bid
  print(bid_higher)
  bid_again = input("Are there other bidders? Type 'yes' or 'no'.\n").lower()
  if bid_again == "no":
    other_bidders = False
    find_highest(bid_higher)
  elif bid_again == "yes":
    other_bidders = True
    # clear()
