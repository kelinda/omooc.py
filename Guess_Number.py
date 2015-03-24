# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

### globals
target = 0
rangeUpperLimit = 0
guessCnt = 0

### helper functions
def gen_new_random(begin, end):
    return random.randint(begin, end)

def new_game():
    # initialize global variables used in your code here
    global target
    global rangeUpperLimit
    global guessCnt
    target = gen_new_random(1, rangeUpperLimit)
    guessCnt = 0
    return

def you_loss():
    print "you loss, do you give in?"

    timer.stop()
    return

### define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global rangeUpperLimit
    rangeUpperLimit = 100
    new_game()
    timer.start()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global rangeUpperLimit
    rangeUpperLimit = 1000
    new_game()
    timer.start()

def judge_guess(guess):
    global target
    global rangeUpperLimit
    global guessCnt
    
    if target == 0:
        print "You haven't choose the range"
        return
    
    if not guess.isdigit():
        print "Please input a number!"
        timer.stop()
        timer.start()
        return
    
    guessCnt += 1
    performance = 0    
    if rangeUpperLimit == 100:
        if guessCnt > 10:
            performance = -1
    if rangeUpperLimit == 1000:
        if guessCnt > 13:
            performance = -1
    if performance == -1:
        print "you loss, do you give in?"
        target = 0
        timer.stop()
        return
    
    if int(guess) == target:
#        global target
        if rangeUpperLimit == 100: 
            if guessCnt <= 5:            
                performance = 10
            else:
                performance = 6
        if rangeUpperLimit == 1000:
            if guessCnt <= 7:
                performance = 10
            else:
                performance = 6
        if performance == 10:
            print "you are genius!"
        else:
            print "bingo! Come on."
        target = 0
        timer.stop()
        return
    if int(guess) < target:
        print "higher"
    else:
        print "lower"
    timer.stop()
    timer.start()
    return
    
def boring():
    print "> What are you thinking about ?!"
    
def stopTimer():
    global target
    if target == 0:
        print "> We haven't started ..."
        return
    timer.stop()
    print 'bye!'
    
# create frame
frame = simplegui.create_frame("Guess Num Game", 150, 180)
frame.set_canvas_background("white")

timer = simplegui.create_timer(10000, boring)


# register event handlers for control elements and start frame
frame.add_button("Guess range (1-100)", range100, 200)
frame.add_button("Guess range (1-1000)", range1000, 200)
frame.add_input("Input your guess:", judge_guess, 195)
frame.add_button("Stop guessing", stopTimer, 120)

frame.start()
