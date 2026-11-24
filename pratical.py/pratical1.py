
import random

# 1. Get computer choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


# 2. Get player choice
def get_player_choice():
    player = input("Enter rock, paper or scissors: ").lower()
    return player


# 3. Check winner
def check_winner(player, computer):
    if player == computer:
        return "It's a Draw!"

    elif player == "rock" and computer == "scissors":
        return "You Win!"

    elif player == "scissors" and computer == "paper":
        return "You Win!"

    elif player == "paper" and computer == "rock":
        return "You Win!"

    else:
        return "Computer Wins!"


# 4. Play game
def play_game():
    player = get_player_choice()
    computer = get_computer_choice()

    print("Player choice:", player)
    print("Computer choice:", computer)

    result = check_winner(player, computer)
    print(result)


# 5. Main function
def main():
    print("===== ROCK PAPER SCISSORS =====")
    play_game()


main()


