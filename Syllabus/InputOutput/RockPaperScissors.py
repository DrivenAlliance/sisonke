from random import randint

game_options = ["Rock", "Paper", "Scissors"]

computer = game_options[randint(0, 2)]

player = raw_input("Rock, Paper or Scissors? ")
print "You played: " + player
print "Computer played: " + computer

if player == computer:
    print("It's a tie!")
elif player == "Rock":
    if computer == "Paper":
        print("You lose!", computer + " covers " + player)
    else:
        print("You win!", player + " crushes " + computer)
elif player == "Paper":
    if computer == "Rock":
        print("You win!", player + " covers " + computer)
    else:
        print("You lose!", computer + " cuts " + player)
elif player == "Scissors":
    if computer == "Rock":
        print("You lose!", computer + " crushes " + player)
    else:
        print("You win!", player + " cuts " + computer)
else:
    print("Invalid play. double check your spelling")
