# This script is an assignment for the Interactive Programming in Python Part 1 from Rice University
# It is been developped within an specific IDE for this curse and might only run within it's platform
# The original code is found here: http://www.codeskulptor.org/#user41_71OyB3fx6J_2.py


# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def get_figures():
    """return the figures dictionary as name: num"""

    figures = {
            'rock': 0,
            'spock': 1,
            'paper': 2,
            'lizard': 3,
            'scissors': 4,
            }
    return figures

def name_to_number(name):
    """return the number of the given figure name or error"""

    figures = get_figures()
    return int(figures.get(name.lower(), "error"))



def number_to_name(number):
    """return the name of the given number figure or error"""

    figures = get_figures()
    inv_figures = dict((v,k) for k, v in figures.items())
    return inv_figures.get(int(number), "error")


def rpsls(player_choice): 
    """rpsls game"""

    figures = get_figures()

    # print a blank line to separate consecutive games
    print("")

    # print out the message for the player's choice
    print("Player chooses " + player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    computer_number = random.randrange(int(figures.values()[0]), int(figures.values()[len(figures)-1]) +1)

    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(computer_number)

    # print out the message for computer's choice
    print("Computer chooses " + computer_choice)

    # compute difference of comp_number and player_number modulo five
    result = (computer_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    if(result == 0):
        print("Player and computer tie!")
    elif(result > 2):
        print("Player wins!")
    else:
        print("Computer wins!")

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
