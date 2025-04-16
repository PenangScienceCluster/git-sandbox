import random

def create_deck():
    """Creates a standard 52-card deck."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]

def calculate_hand_value(hand):
    """Calculates the value of a hand in Blackjack."""
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    value = 0
    aces = 0

    for card in hand:
        rank = card.split(' ')[0]
        value += rank_values[rank]
        if rank == 'Ace':
            aces += 1

    # Adjust for Aces if value exceeds 21
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

def blackjack():
    print("Welcome to Blackjack!")
    deck = create_deck()
    random.shuffle(deck)

    # Deal initial hands
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print(f"Your hand: {', '.join(player_hand)} (Value: {calculate_hand_value(player_hand)})")
    print(f"Dealer's visible card: {dealer_hand[0]}")

    # Player's turn
    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
            print(f"Your hand: {', '.join(player_hand)} (Value: {calculate_hand_value(player_hand)})")
        elif action == 'stand':
            break
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")

    player_value = calculate_hand_value(player_hand)
    if player_value > 21:
        print("You busted! Dealer wins.")
        return

    # Dealer's turn
    print(f"\nDealer's hand: {', '.join(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})")
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print(f"Dealer's hand: {', '.join(dealer_hand)} (Value: {calculate_hand_value(dealer_hand)})")

    dealer_value = calculate_hand_value(dealer_hand)
    if dealer_value > 21:
        print("Dealer busted! You win!")
    elif dealer_value > player_value:
        print("Dealer wins!")
    elif dealer_value < player_value:
        print("You win!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    blackjack()