import random

#  Your cards: [6, 8], current score: 14
#    Computer's first card: 7
# Type 'y' to get another card, type 'n' to pass: n
#    Your final hand: [6, 8], final score: 14
#    Computer's final hand: [7, 7, 10], final score: 24
# Opponent went over. You win 😁
# Do you want to play a game of Blackjack? Type 'y' or 'n': 

def cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 10, 10]
    return cards
def computer_card(ComCard, comscore):
    for n in cards():
        if comscore < 17:
            computer_draw_card = random.choice(cards())
            ComCard += [computer_draw_card]
            comscore = sum(ComCard)
    return {"comp_score": comscore, "comp_card": ComCard}
    #     elif comscore > 21:
    #         print(f"Computer final hand: {ComCard}, final score: {comscore}")
    #         print("Your opponent went over, You win")
    #         black_jack()
    # print(f"Computer final hand: {ComCard}, final score: {comscore}")

def user_cards(ucard, uscore, comscore, another_round ):
    if another_round == 'n':
        return ucard, uscore
    elif uscore < 21:
        user_draw_card = random.choice(cards())
        ucard +=[user_draw_card]
        uscore = sum(ucard)
        print(f"Your current cards: {ucard}, current score: {uscore}")
        if uscore != 21 and uscore < 21:    
            print(f"Computer's first card: {comscore[0]}")

    elif ucard == [11, 10]:
        print(f"Your final hand: {ucard}, final score: {uscore}")
    elif uscore > 21:
        if 11 in ucard:
            uscore -= 10
            if uscore > 21:
                print(f"Your final hand: {ucard}, final score: {uscore}")
        else:
            print(f"Your final hand: {ucard}, final score: {uscore}")
            
        
def black_jack():
    start = input("Do you want to play BlackJack, Type 'y' to play or 'n' to exit: ").lower()
    if start == 'y':
        cards()
        user = random.sample(cards(), 2)
        computer = random.sample(cards(), 2)
        # user = [7, 10]
        # computer = [2, 10]
        user_score = sum(user)
        computer_score = sum(computer)
        print(f"Your cards: {user}, current score: {user_score}\nComputer's first card: {computer[0]}")
        hit = True
        while hit:
            user_score = sum(user)
            computer_score = sum(computer)
            if user == [11, 10] and computer == [11, 10]:
                user_cards(ucard=user, uscore=user_score, comscore=computer, another_round=another_card)
                computer_card(ComCard=computer, comscore=computer_score)
                print("Draw")
                black_jack() 
            elif user == [11, 10] or user_score == 21:
                user_cards(ucard=user, uscore=user_score, comscore=computer, another_round=another_card)
                computer_card(ComCard=computer, comscore=computer_score)
                print("You win!")
                black_jack() 
            elif computer == [11, 10] or computer_score == 21:
                user_cards(ucard=user, uscore=user_score, comscore=computer, another_round=another_card)
                computer_card(ComCard=computer, comscore=computer_score)
                print("Computer Win!")
                black_jack() 
            elif user_score > 21:
                # user_cards(ucard=user, uscore=user_score, comscore=computer, another_round=another_card)
                computer_card(ComCard=computer, comscore=computer_score)
                print("You went over, You lose!") 
                black_jack()     
            another_card = input("Type 'y' for another card and 'n' for pass: ")
            if another_card == 'y':
                user_cards(ucard=user, uscore=user_score, comscore=computer, another_round=another_card)
                computer_card(ComCard=computer, comscore=computer_score)
            elif another_card == 'n':
                comp = computer_card()
                if comp["comp_score"] > 21:
                    print(comp["comp_score"])

             
black_jack()


############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt