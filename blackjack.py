import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def display_table(player_cards, computer_cards, is_game_over):
    print(f"Your cards: {player_cards}, Total Score: {calculate_score(player_cards)}")
    if is_game_over:
        print(f"Computer's cards: {computer_cards}, Total Score: {calculate_score(computer_cards)}")
    else:
        print(f"Computer's cards: [{computer_cards[0]}, ?]")

def play_blackjack():
    while True:
        user_cards = []
        computer_cards = []
        game_over = False

        for n in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            display_table(user_cards, computer_cards, game_over)

            if user_score == 0 or computer_score == 0 or user_score > 21:
                game_over = True
            else:
                ask = input('Do you want to draw another card? Type "Y" or "N": ')
                if ask.lower() == 'y':
                    user_cards.append(deal_card())
                else:
                    game_over = True

            if computer_score < 17 and not game_over:
                computer_cards.append(deal_card())

        display_table(user_cards, computer_cards, game_over)
        compare(user_score, computer_score)

        play_again = input("Do you want to play again? Type 'Y' or 'N': ")
        if play_again.lower() != 'y':
            break

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's a draw!")
    elif computer_score == 0:
        print("You lose! Computer has a Blackjack.")
    elif user_score == 0:
        print("You win! You have a Blackjack.")
    elif user_score > 21:
        print("You lose! You went over 21.")
    elif computer_score > 21:
        print("You win! Computer went over 21.")
    elif computer_score >= 17 and computer_score >= user_score:
        print("You lose! Computer has a higher score.")
    elif user_score > computer_score:
        print("You win! You have a higher score.")

play_blackjack()
