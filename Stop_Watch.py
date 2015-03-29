# template for "Stopwatch: The Game"

import simplegui

# define global variables
milisecond = 0
win_cnt = 0
tot_cnt = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def time_format(t):
    minute = t / 1000 / 60
    second = (t / 1000 - minute * 60)
    milisec = (t % 1000) / 100
    trimg = "%(minute)02d:%(second)02d.%(milisec)d"%{"minute":minute, "second":second, "milisec":milisec}
    return trimg
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startTick():
    timer.start()

def stopTick():
    global win_cnt, tot_cnt
    timer.stop()
    tot_cnt += 1
    if milisecond % 1000 == 0:
        win_cnt += 1

    
def reTick():
    global milisecond
    global win_cnt, tot_cnt
    milisecond = 0    
    win_cnt = 0
    tot_cnt = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global milisecond
    milisecond += 100

# define draw handler
def draw_time(canvas):
    canvas.draw_text(time_format(milisecond), [135, 140], 40, "pink")
    canvas.draw_text(str(win_cnt)+'/'+str(tot_cnt), [350, 40], 25, "white")
    return
    
# create frame
frame = simplegui.create_frame("Stop Whatch", 400, 250)
frame.set_canvas_background("grey")
frame.add_button("Start", startTick, 100)
frame.add_button("Stop", stopTick, 100)
frame.add_button("Reset", reTick, 100)

timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw_time)


# start frame
frame.start()


# Please remember to review the grading rubric
