# -*- coding: utf-8 -*-

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math


# intialize globals
width = 600
height = 500
draw_list = []
draw_radius = 10
draw_color = "rgba(255, 0, 0, 0.05)"
draw_shape = "circle"
order = 0
review_list = []
step = 0
interval = 500
# helper function

#def distance(p, q):
#    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

    
# define event handler for button
def click_circle():
    global  draw_shape
    draw_shape = "circle"

def click_triangle():
    global  draw_shape
    draw_shape = "triangle"

def click_square():
    global draw_shape
    draw_shape = "square"

def click_red():
    global draw_color
    draw_color = "rgba(255, 0, 0, 0.05)"

def click_blue():
    global draw_color
    draw_color = "rgba(0, 0, 255, 0.05)"

def click_green():
    global draw_color
    draw_color = "rgba(0, 255, 0, 0.05)"


# define event handler for mouse click, draw
def click(pos):
    global draw_pos , draw_shape , draw_radius , draw_color , order , review_list , timer
    #防止在回放时点击画布输入图案，扰乱回放过程。
    
    if timer.is_running():
        return
    x = pos[0]
    y = pos[1]
    n = draw_radius
    
    if draw_shape == "circle":
            pos = [x , y]
    elif draw_shape == "triangle":
#            pos = [(x, y-n),(x+n,y+n/2),(x-n,y+n/2)]
            pos = [x, y]
    elif draw_shape == "square":
#            pos = [[x-n,y-n],[x+n,y-n],[x+n,y+n],[x-n,y+n]]
            pos = [x, y]
           
    order += 1
    if order <= 1024:
        draw_list.append([pos,draw_shape,draw_color])
        
    review_list = draw_list
    return review_list
    
def draw(canvas):
    global draw_pos , draw_shape , draw_radius , draw_color , len1 , len2 
    for draw_pos in draw_list:
        if draw_pos[1] == "circle":
            for r in range(1, draw_radius+1):
                canvas.draw_circle(draw_pos[0], r, 1 , draw_pos[2], draw_pos[2])
        else:
            if draw_pos[1] == "triangle":
                x = draw_pos[0][0]
                y = draw_pos[0][1]
                for r in range(1, draw_radius+1):
                    canvas.draw_polygon([(x, y-r),(x+r,y+r/2),(x-r,y+r/2)], 1 , draw_pos[2], draw_pos[2])              
                
            if draw_pos[1] == "square":
                x = draw_pos[0][0]
                y = draw_pos[0][1]
                for r in range(1, draw_radius+1):
                    canvas.draw_polygon([[x-r,y-r],[x+r,y-r],[x+r,y+r],[x-r,y+r]], 1 , draw_pos[2], draw_pos[2])              
                
def click_review():
        timer.start()
   
def click_acc():
        global timer , interval 
        if timer.is_running():
            timer.stop()
            #防止变量变为0
            interval = interval/2 + 1
            timer = simplegui.create_timer(interval, timer_handler)
            timer.start()
            
def click_dec():
    global timer, interval
    if timer.is_running():
        timer.stop()
        interval = interval + 200
        timer = simplegui.create_timer(interval, timer_handler)
        timer.start()
            
def click_stop():
    timer.stop()
        
def click_output():
    pass
           
def timer_handler():
    global draw_pos , draw_list , review_list , order , step
    draw_list = []
    order = len(review_list)
    if step < order :
        step += 1 
        for review_step in range(0,step):
            if review_step < len(review_list):
                 draw_list.append(review_list[review_step])    
        #return [review_step for review_step in range(0,step) if review_step <len(review_list)]          
    else:
        step = 0
    pass


# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

frame.add_button("Circle\n",click_circle,100)
frame.add_button("Triangle\n",click_triangle,100)
frame.add_button("Square\n",click_square,100)
frame.add_label("", 100)
frame.add_button("Red\n",click_red,100)
frame.add_button("Blue\n",click_blue,100)
frame.add_button("Green\n",click_green,100)
frame.add_label("", 100)
frame.add_button("Play\n",click_review,80)
frame.add_button("Accelarate\n",click_acc,80)
frame.add_button("Decel\n",click_dec,80)
frame.add_button("Stop\n",click_stop,80)
frame.add_label("", 100)
frame.add_button("Save\n",click_output,80)

timer = simplegui.create_timer(interval, timer_handler)

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)


# start frame
frame.start()
