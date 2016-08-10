# This script is an assignment for the Interactive Programming in Python Part 1 from Rice University
# It is been developped within an specific IDE for this curse and might only run within it's platform
# The original code is found here: http://www.codeskulptor.org/#user41_TLrox9WOLy_6.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

number = 0
message = ""
counter = 0
size = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global number, counter, message
    number = 0
    counter = 0
    message = " "

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [60,112], size, "White")

# set the message
def set_message(msg, s):
    global message, size
    message = msg
    size = s
    print msg

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number
    new_game()
    number = random.randrange(0,100)
    set_message("I've set a number from 0-100, guess it!",34)


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global number
    new_game()
    number = random.randrange(0,1000)
    set_message("I've set a number from 0-1000, guess it!",34)

def input_guess(guess):
    global number, counter

    counter += 1
    # main game logic goes herecontext
    print "Guess was " + guess
    if(int(guess) == number):
        set_message("Correct! in " + str(counter) + " times",50)
    elif(int(guess) > number):
        set_message("Lower",55)
    else:
        set_message("Higher",55)


# create frame
frame = simplegui.create_frame('Guess my number', 800, 500)
frame.add_button('range 100', range100)
frame.add_button('range 1000', range1000)
frame.add_input('your guess', input_guess, 100)
frame.set_draw_handler(draw)
frame.start()

# register event handlers for control elements and start frame


# call new_game 
new_game()
