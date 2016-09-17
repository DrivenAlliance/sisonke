#note: This is not meant to be a perfect example of clean code, or close to it..Is is however meant to be an example of Rock Paper Scissors with the options read from a file
from random import randint

def read_game_state():
    game_options = []
    result_decisions = []
    with open("gamestate.txt") as game_state_file:
        game_options = game_state_file.readline().split(",")
        for line in game_state_file:
            result_decision = line.split(",")
            print("incoming line: %s" % result_decision)
            result_decisions.append({'Player': result_decision[0], 'Computer':result_decision[1], 'Winner': result_decision[2].replace("\n","")})
    return game_options, result_decisions

def get_decision(result_decisions):
    for decision in result_decisions:
        if decision["Player"] == player_choice and decision["Computer"] == computer_choice:
            print "You played: %s, Computer Played %s which means %s" % (player_choice, computer_choice, decision["Winner"])
            return
    print("We could not find option for player: %s computer %s" % (player_choice, computer_choice))

def get_computer_choice(game_options):
    return game_options[randint(0, 2)]

def get_player_choice():
    return raw_input("Rock, Paper or Scissors? ")

game_options, result_decisions = read_game_state()

computer_choice = get_computer_choice(game_options)
player_choice = get_player_choice()

print("Computer choice: %s" % computer_choice)
print("Player_choice choice: %s" % player_choice)

get_decision(result_decisions)

