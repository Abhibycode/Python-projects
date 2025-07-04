import random

card = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

def card_value(pick):
    """Helper function to get the numeric value of a card."""
    if pick in ("K", "Q", "J"):
        return 10
    elif pick == "A":
        return 1  # Or 11, depending on the game's rules
    else:
        return pick

def deal_initial_cards():
    """Deals two cards to the user and the computer."""
    user_cards = [random.choice(card), random.choice(card)]
    computer_cards = [random.choice(card), random.choice(card)]
    return user_cards, computer_cards

def calculate_score(cards):
    """Calculates the score of a hand of cards."""
    score = 0
    for pick in cards:
        score += card_value(pick)
    return score

def display_cards(user_cards, computer_cards, show_computer_first_card=True):
    """Displays the cards of the user and computer."""
    print("Your cards:", " ".join(map(str, user_cards)))  # Use map to convert to strings
    if show_computer_first_card:
        print("Computer's first card:", computer_cards[0])
    else:
        print("Computer's cards:", " ".join(map(str, computer_cards)))

def play_game():
    """Main function to play a simplified Blackjack game."""

    user_cards, computer_cards = deal_initial_cards()
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("Initial deal:")
    display_cards(user_cards, computer_cards, show_computer_first_card=True)
    print("Your score:", user_score)

    # User's turn
    while user_score < 21:
        action = input("Do you want to hit or stand? (h/s): ")
        if action.lower() == 'h':
            user_cards.append(random.choice(card))
            user_score = calculate_score(user_cards)
            display_cards(user_cards, computer_cards, show_computer_first_card=True)
            print("Your score:", user_score)
        elif action.lower() == 's':
            break
        else:
            print("Invalid action. Please enter 'h' or 's'.")

    # Computer's turn (simple strategy)
    while computer_score < 17:  # Computer hits below 17
        computer_cards.append(random.choice(card))
        computer_score = calculate_score(computer_cards)

    print("\nGame Over")
    display_cards(user_cards, computer_cards, show_computer_first_card=False)
    print("Your final score:", user_score)
    print("Computer's final score:", computer_score)

    # Determine winner
    if user_score > 21:
        print("You bust! You lose.")
    elif computer_score > 21:
        print("Computer busts! You win.")
    elif user_score > computer_score:
        print("You win!")
    elif computer_score > user_score:
        print("You lose.")
    else:
        print("It's a draw.")

# Start the game
play_game()