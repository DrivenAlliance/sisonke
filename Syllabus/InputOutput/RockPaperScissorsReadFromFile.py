#note: This is not meant to be a perfect example of clean code, or close to it..Is is however meant to be an example of Rock Paper Scissors with the options read from a file
from random import randint

game_options = []
result_decisions = []

with open("gamestate.txt") as game_state_file:
    game_options = game_state_file.readline().split(",")
    for line in game_state_file:
        result_decision = line.split(",")
        result_decisions.append({'Player': result_decision[0], 'Computer':result_decision[1], 'Winner': result_decision[2].replace("\n","")})

computer = game_options[randint(0, 2)]
player = raw_input("Rock, Paper or Scissors? ")

print "You played: " + player
print "Computer played: " + computer

for decision in result_decisions:
    if decision["Player"] == player and decision["Computer"] == computer:
        print "%s" % decision["Winner"]
        break
