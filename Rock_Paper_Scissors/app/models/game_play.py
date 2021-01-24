from app.models.player import Player
from app.models.game import Game

players = []

def add_player(player):
    players.append(player)

def game_result(choice1, choice2):
    if choice1 == choice2:
        return "Shan times, it's a tie"
    elif choice1 == "rock" and choice2 == "paper":
        return f"Player 2 wins by playing {choice2}"
    elif choice1 == "rock" and choice2 == "scissors":
        return f"Player 1 wins by playing {choice1}"
    elif choice1 == "paper" and choice2 == "scissors":
        return f"Player 2 wins by playing {choice2}"
    elif choice1 == "paper" and choice2 == "rock":
        return f"Player 1 wins by playing {choice1}"
    elif choice1 == "scissors" and choice2 == "rock":
        return f"Player 2 wins by playing {choice2}"
    elif choice1 == "scissors" and choice2 == "paper":
        return f"Player 1 wins by playing {choice1}"   
    else:
        return "please enter rock, paper, or scissors"