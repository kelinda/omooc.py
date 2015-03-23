
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

### globals
target = 0
rangeUpperLimit = 0

inp = 0

### helper functions
def gen_new_random(begin, end):
    return random.randint(begin, end)

def new_game():
    # initialize global variables used in your code here
    global target
    global rangeUpperLimit
    print "new game"
    target = gen_new_random(1, rangeUpperLimit)
    print target
    return
    
### define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global rangeUpperLimit
    rangeUpperLimit = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global rangeUpperLimit
    rangeUpperLimit = 1000
    new_game()    

def judge_guess(guess):
    global target
    if target == 0:
        print "You haven't choose the range"
        return
    if int(guess) == target:
#        global target
        print "bingo!"
        target = 0
        return
    if int(guess) < target:
        print "higher"
    else:
        print "lower"
    return
    
    
# create frame
frame = simplegui.create_frame("Guess Num Game", 250, 250)
frame.set_canvas_background("white")


# register event handlers for control elements and start frame
frame.add_button("range(1-100)", range100, 200)
frame.add_button("range(1-1000)", range1000, 200)
inp = frame.add_input("Input your guess", judge_guess, 200)


frame.start()
