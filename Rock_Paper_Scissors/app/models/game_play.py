from app.models.player import Player
from app.models.game import Game

players = []

def add_player(player):
    players.append(player)

# def game_result(choice1, choice2):
#     if choice1 == choice2:
#         return "Shan times, it's a tie"
#     elif choice1 == "rock" and choice2 == "paper":
#         return f"Player 2 wins by playing {choice2}"
#     elif choice1 == "rock" and choice2 == "scissors":
#         return f"Player 1 wins by playing {choice1}"
#     elif choice1 == "paper" and choice2 == "scissors":
#         return f"Player 2 wins by playing {choice2}"
#     elif choice1 == "paper" and choice2 == "rock":
#         return f"Player 1 wins by playing {choice1}"
#     elif choice1 == "scissors" and choice2 == "rock":
#         return f"Player 2 wins by playing {choice2}"
#     elif choice1 == "scissors" and choice2 == "paper":
#         return f"Player 1 wins by playing {choice1}"   
#     else:
#         return "please enter rock, paper, or scissors"

def name_result(player1, player2):
    if player1.choice == player2.choice:
        return "Shan times, it's a tie"
    elif player1.choice == "rock" and player2.choice == "paper":
        return f"{player2.name} wins by playing {player2.choice}"
    elif player1.choice == "rock" and player2.choice == "scissors":
        return f"{player1.name} wins by playing {player1.choice}"
    elif player1.choice == "paper" and player2.choice == "scissors":
        return f"{player2.name} wins by playing {player2.choice}"
    elif player1.choice == "paper" and player2.choice == "rock":
        return f"{player1.name} wins by playing {player1.choice}"
    elif player1.choice == "scissors" and player2.choice == "rock":
        return f"{player2.name} wins by playing {player2.choice}"
    elif player1.choice == "scissors" and player2.choice == "paper":
        return f"{player1.name} wins by playing {player1.choice}"   
    else:
        return "No-one! Please enter rock, paper, or scissors"