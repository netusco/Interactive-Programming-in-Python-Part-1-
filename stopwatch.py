# This script is an assignment for the Interactive Programming in Python Part 1 from Rice University
# It is been developped within an specific IDE for this curse and might only run within it's platform
# The original code is found here: http://www.codeskulptor.org/#user41_CkrpsCEOUV_3.py


# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
started = False
success = 0
stopped = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    min = int(t/600)
    dt = t - (600 * min)
    if(len(str(dt)) < 3):
        sec = '0' + str(dt)[0]
    else:
        sec = str(dt)[0:2]
    ftime = str(min) + ':' + sec + '.' + str(dt)[-1]

    return str(ftime)


# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler_reset():
    global time, stopped, started, success
    timer.stop()
    stopped = 0
    success = 0
    started = False
    time = 0

def button_handler_start():
    global timer, started
    started = True
    timer.start()

def button_handler_stop():
    global timer, stopped, started, success
    if(started): 
        stopped += 1
        if(int(str(time)[-1]) == 0):
            success += 1
    started = False
    timer.stop()
    format(time)

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time +=1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), [300, 250], 80, 'White')
    canvas.draw_text(str(success) + '/' + str(stopped), [680, 40], 30, 'Yellow')

# create frame
frame = simplegui.create_frame('Testing', 750, 500)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)
bStart = frame.add_button('Start', button_handler_start)
bStop = frame.add_button('Stop', button_handler_stop)
bReset = frame.add_button('Reset', button_handler_reset)

# start frame
frame.start()
