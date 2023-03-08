import random

options = (
    "rock",
    "paper",
    "scissors"
)
player = None
computer = random.choice(options)
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice [Rock, Paper, Scissors]: ")

    print(f"Player: {player.capitalize()}")
    print(f"Computer: {computer.capitalize()}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You lose :(")

    if not input("Play Again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")

