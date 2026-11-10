import random

# The three possible moves and the starting scores
moves = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

# Play 5 rounds
for round_number in range(1, 6):
    print("--- Round", round_number, "---")
    
    # Ask untill the player types a valid move
    player = ""
    while player not in moves:
        player = input("Choose rock, paper or scissors: ").lower().strip()
        if player not in moves:
            print("That is not a valid move. Try again.")
    
    # The computer picks a random move
    computer = random.choice(moves)
    print("You chose:", player)
    print("Computer chose:", computer)

    # Decide who wins the round and update the score
    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win this round!")
        player_score = player_score + 1
    elif player == "paper" and computer == "rock":
        print("You win this round!")
        player_score = player_score + 1
    elif player == "scissors" and computer == "paper":
        print("You win this round!")
        player_score = player_score + 1
    else:
        print("Computer wins this round!")
        computer_score = computer_score + 1
        
# Show the final score and the winner
print("Final score: You", player_score, "- Computer", computer_score)

if player_score > computer_score:
    print("You won the game!")
elif player_score < computer_score:
    print("The computer won the game.")
else:
    print("The game is a draw.")