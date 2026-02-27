import random

print("Welcome to Blackjack!")
print(
    "Please note: this is not an ordinary game of blackjack.\n"
    "For programming simplicity, assume there is an infinite number of cards in the deck.\n"
    "Assume all cards played get reshuffled after every play.\n"
    "There are no jokers in the deck.\n"
    "You cannot split your hand (yet).\n"
    "Good luck!\n"
)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def hand_total(hand):
    """Return best total <= 21 if possible, by converting Aces 11 -> 1 as needed."""
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces > 0:
        total -= 10  # convert one Ace from 11 to 1
        aces -= 1
    return total

def display_hand(prefix, hand, hide_first=False):
    if hide_first:
        shown = ["?"] + [str(c) for c in hand[1:]]
        print(f"{prefix}: [{'], ['.join(shown)}]")
    else:
        print(f"{prefix}: [{'], ['.join(str(c) for c in hand)}] (total: {hand_total(hand)})")

# --- Start a single round ---
player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

display_hand("You have", player_hand)
display_hand("Dealer shows", dealer_hand, hide_first=True)

player_total = hand_total(player_hand)
dealer_total = hand_total(dealer_hand)

# --- Check initial blackjack cases ---
if dealer_total == 21 and player_total == 21:
    display_hand("Dealer has", dealer_hand)
    print("Dealer and player have blackjack! It's a draw!")
elif dealer_total == 21:
    display_hand("Dealer has", dealer_hand)
    print("Dealer had blackjack! You lose!")
elif player_total == 21:
    print("Blackjack! You win!")
else:
    # --- Player turn ---
    while True:
        choice = input("Would you like to hit or stand? ").strip().lower()
        if choice not in {"hit", "stand"}:
            print("Please type 'hit' or 'stand'.")
            continue

        if choice == "hit":
            player_hand.append(deal_card())
            display_hand("You have", player_hand)
            player_total = hand_total(player_hand)

            if player_total > 21:
                print("You busted! You lose!")
                break
        else:
            print(f"You stand at {hand_total(player_hand)}.")
            break

    # --- Dealer turn (only if player didn't bust) ---
    if hand_total(player_hand) <= 21:
        display_hand("Dealer reveals", dealer_hand)

        while hand_total(dealer_hand) < 17:
            dealer_hand.append(deal_card())
            display_hand("Dealer draws", dealer_hand)

        dealer_total = hand_total(dealer_hand)
        player_total = hand_total(player_hand)

        # --- Compare totals ---
        if dealer_total > 21:
            print("Dealer busted! You win!")
        elif dealer_total > player_total:
            print(f"Dealer has {dealer_total}, you have {player_total}. You lose!")
        elif dealer_total < player_total:
            print(f"Dealer has {dealer_total}, you have {player_total}. You win!")
        else:
            print(f"Dealer has {dealer_total}, you have {player_total}. It's a draw!")