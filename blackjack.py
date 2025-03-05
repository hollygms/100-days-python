import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



#functions

def ace_in_hand(hand, score):
        score = sum(hand)
        for card in hand:
            if card == 11 and score >21:
                    card_index = hand.index(card)
                    hand[card_index] = 1
            score = sum(hand)
        return hand


def draw_user_card():
    #first loop
    user_answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if user_answer == "y":
        print("\n" * 20)
        print(art.logo)
    else:
        return
    user_hand =  [random.choice(cards)]
    if len(user_hand) < 2:
        user_hand.append(random.choice(cards))
    user_score = sum(user_hand)
    ace_in_hand(user_hand, user_score)
    user_score = sum(user_hand)
    print(f"Your cards: {user_hand}, current score: {user_score}")
    dealer_hand = [random.choice(cards)]
    dealer_score = sum(dealer_hand)
    print(f"Computer's first card: {dealer_hand}")
    #loops
    while user_score <= 21:
        user_answer = input(f"Type 'y' to get another card. Type 'n' to pass: ")
        if user_answer == "y":
            user_hand.append(random.choice(cards))
            user_hand = ace_in_hand(user_hand, user_score)
            user_score = sum(user_hand)
            print(f"Your cards: {user_hand}, current score: {user_score}")
            print(f"Computer's first card: {dealer_hand}")
        else:
            break
    while dealer_score < 17 and user_score <= 21:
        dealer_hand.append(random.choice(cards))
        dealer_hand = ace_in_hand(dealer_hand, dealer_score)
        dealer_score = sum(dealer_hand)
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")
    if user_score > 21:
        print("You lose!")
    elif dealer_score > 21:
        print("You win!")
    elif user_score == dealer_score:
        print("It's a draw")
    else:
        if (21 - user_score) < (21 - dealer_score):
            print("You won!")
        else:
            print("You lose!")

    draw_user_card()





draw_user_card()



