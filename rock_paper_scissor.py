import random

computer = random.choice(['r', 'p', 's'])
user = input("Choose 'r' for rock, 'p' for paper or 's' for scissor: ")

def play():
    if computer == user:
        return "It's a tie"

    if is_won(user,computer):
        return 'You won'
    return 'You lost'

def is_won(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return(True)

print(play())

