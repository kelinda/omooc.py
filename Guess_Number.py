# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

### globals
target = 0            # the number computer hold
rangeUpperLimit = 0   # 1-rangeUpperLimit is the guess range.
guessCnt = 0          # how many times user have guessed.

lineNumber = 0        # line number of output on the canvas.
textSize = 15          # each character will take textSize pixels on canvas.
lineHeight = textSize + 5
canvasHeight = 400    # canvas height in pixels
canvasWidth = 250
maxLineNumber = canvasHeight / lineHeight

outputStrings = []    # store all the outputs in current canvas.

### helper functions
def gen_new_random(begin, end):
    return random.randint(begin, end)

# init the game parameters
def new_game():
    # initialize global variables used in your code here
    global target
    global rangeUpperLimit
    global guessCnt
    target = gen_new_random(1, rangeUpperLimit)
    guessCnt = 0
    return

# print to canvas, not the console
def print_to_canvas(str):
    global maxLineNumber
    global lineNumber
    global outputStrings
    
    outputStrings += [str]
    lineNumber += 1
    if lineNumber > maxLineNumber:
        outputStrings = outputStrings[1:len(outputStrings)]
    return
    

### define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global rangeUpperLimit
    rangeUpperLimit = 100
    new_game()
    print_to_canvas( "game start!")
    timer.start()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global rangeUpperLimit
    rangeUpperLimit = 1000
    new_game()
    print_to_canvas( "game start!")
    timer.start()

def judge_guess(guess):
    global target
    global rangeUpperLimit
    global guessCnt
    
    if target == 0:
        print_to_canvas( "You haven't choose the range")
        return
    
    if not guess.isdigit():
        print_to_canvas("Please input a number!")
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
        print_to_canvas("you loss, do you give in?")
        target = 0
        timer.stop()
        return
    
    if int(guess) == target:
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
            print_to_canvas("you are genius!")
        else:
            print_to_canvas("bingo! Come on.")
        target = 0
        timer.stop()
        return
    if int(guess) < target:
        print_to_canvas("higher")
    else:
        print_to_canvas("lower")
    timer.stop()
    timer.start()
    return
    
def boring():
    print_to_canvas("> What are you thinking about ?!")
    
def stopTimer():
    global target
    if target == 0:
        print_to_canvas("> We haven't started ...")
        return
    timer.stop()
    print_to_canvas("bye!")
    
    
# define draw handler
def result_reporter(canvas):    
    global outputStrings
    global lineHeight
    
    localLineNumber = 1        
    for outputLine in outputStrings:
        canvas.draw_text(outputLine, [0, localLineNumber*lineHeight], textSize, "blue")
        localLineNumber += 1
    return

    
# create frame
frame = simplegui.create_frame("Guess Num Game", canvasWidth, canvasHeight + textSize/2)
frame.set_canvas_background("white")
frame.set_draw_handler(result_reporter)

timer = simplegui.create_timer(10000, boring)


# register event handlers for control elements and start frame
frame.add_button("Guess range (1-100)", range100, 200)
frame.add_button("Guess range (1-1000)", range1000, 200)
frame.add_input("Input your guess:", judge_guess, 195)
frame.add_button("Stop guessing", stopTimer, 120)

frame.start()
