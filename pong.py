# This script is an assignment for the Interactive Programming in Python Part 1 from Rice University
# It is been developped within an specific IDE for this curse and might only run within it's platform
# The original code is found here: http://www.codeskulptor.org/#user41_cfVUpWNQGl_7.py


# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 1650
HEIGHT = 950
BALL_RADIUS = 20
PAD_WIDTH = 10
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = HEIGHT/2 - PAD_HEIGHT/2
paddle2_pos = HEIGHT/2 - PAD_HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 9
ball_pos = [WIDTH/2, HEIGHT/2]
time = 0
ball_vel = [0,0]
ball_vel_range = [7, 10]
score1 = 0
score2 = 0
score_size = 300

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if(LEFT):
        hor = -1
        vert = 1
    else:
        hor = 1
    vert = -1
    ball_vel[0] = random.randrange(ball_vel_range[0], ball_vel_range[1]) * hor
    ball_vel[1] = random.randrange(ball_vel_range[0], ball_vel_range[1]) * (-1)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_pos = HEIGHT/2 - PAD_HEIGHT/2
    paddle2_pos = HEIGHT/2 - PAD_HEIGHT/2
    spawn_ball()

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global LEFT, RIGHT


    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]

    # bounce ball if touches the vertical walls
    if(ball_pos[1] - BALL_RADIUS < 0 or
        ball_pos[1] + BALL_RADIUS > HEIGHT):
        ball_vel[1] = ball_vel[1] * (-1)    

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel

    # paddle 1 limits
    if(paddle1_pos < 0):
        paddle1_pos = 0
    elif(paddle1_pos > HEIGHT - PAD_HEIGHT):
        paddle1_pos = HEIGHT - PAD_HEIGHT

    # paddle 2 limits   
    if(paddle2_pos < 0):
        paddle2_pos = 0
    elif(paddle2_pos > HEIGHT - PAD_HEIGHT):
        paddle2_pos = HEIGHT - PAD_HEIGHT

    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos], [PAD_WIDTH, paddle1_pos + PAD_HEIGHT], [0, paddle1_pos + PAD_HEIGHT]], 12, 'White', 'White')
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], [WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT]], 12, 'White', 'White')

    # determine whether paddle and ball collide
    # LEFT
    if((ball_pos[0] - BALL_RADIUS) <= (0 + PAD_WIDTH)):
        if(ball_pos[1] + BALL_RADIUS > paddle1_pos and ball_pos[1] - BALL_RADIUS < (paddle1_pos + PAD_HEIGHT)):
            ball_vel[0] = ball_vel[0] * (-1)
            LEFT = False
            RIGHT = True
        else:
            score2 += 1
            spawn_ball()

    # RIGHT
    elif((ball_pos[0] + BALL_RADIUS) >= (WIDTH - PAD_WIDTH)):
        if(ball_pos[1] + BALL_RADIUS > paddle2_pos and ball_pos[1] - BALL_RADIUS < (paddle2_pos + PAD_HEIGHT)):
            ball_vel[0] = ball_vel[0] * (-1)
            LEFT = True
            RIGHT = False
        else:
            score1 += 1
            spawn_ball()

    # draw scores
    canvas.draw_text(str(score1), [(WIDTH / 4) - (score_size / 3), (HEIGHT / 2) + (score_size / 3)], score_size, "Yellow")
    canvas.draw_text(str(score2), [((WIDTH / 4) * 3) - (score_size / 3), (HEIGHT / 2) + (score_size / 3)], score_size, "Yellow")

def keydown(key):
    global paddle1_vel, paddle2_vel

    # paddle 1 controls
    if key == simplegui.KEY_MAP["a"]:
        paddle1_vel += paddle_vel
    elif key == simplegui.KEY_MAP["q"]:
        paddle1_vel -= paddle_vel

    # paddle 2 controls
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += paddle_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= paddle_vel

def keyup(key):
    global paddle1_vel, paddle2_vel

    # paddle 1 controls
    if key == simplegui.KEY_MAP["a"] or key == simplegui.KEY_MAP["q"]:
        paddle1_vel = 0

    # paddle 2 controls
    if key == simplegui.KEY_MAP["down"] or key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0



# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
