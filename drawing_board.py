import Tkinter as tk

## define globals
bgcolor = "#EEE"

draw_select = 0 #0 for lines, 1 for dots
pen_select = 0 # for line: thin, medicore, thick
               # for dot: triangle, circle, square
color_select = 0 #0 for red, 1 for green, 2 for blue
eraser_select = 0 #0 for thin eraser, 1 for medium, 2 for thick
status_label_list = []

no_draw = False #after select click, do not draw anything

pen_list = ["thin", "medium", "thick"]
color_list = ["red", "green", "blue"]
eraser_list = pen_list
menu_list = [[]] #menu_list ids, subsequence hold drawing-option icon ids.

menu_is_showing = 0 # 0 for no, 1 for yes.
menu_area = [0, 0, 0, 0] # left, top, width, height

option_square_size = 20  # drawing-option icon is square, this is the size.
circle_radius = 5 # circle dots radius
triangle_size = 10 # triangle dot side length
square_size = 10 # square dot side lenght

oldx = 0
oldy = 0

####################
## define helpers ##
####################
def update_status_label():
    global canvas
    global draw_select, pen_select, color_select
    global status_label_list
    for label in status_label_list:
        canvas.delete(label)
    label_text = ''

    if draw_select == 0: #line
        if color_select < 4:
            label_text = 'line'
        else:
            label_text = 'eraser'
    elif draw_select == 1: #dot 
        label_text = 'dot'
    label_id = canvas.create_text(90, 25, anchor=tk.SW, text=label_text, font=('Times', '12'), fill='#888')
    status_label_list[0] = (label_id)

    if pen_select == 0: #circle
        if draw_select == 0:
            label_text = 'thin'
        else: 
            label_text = 'circle'
    elif pen_select == 1: # striganle
        if draw_select == 0:
            label_text = 'medium'
        else: 
            label_text = 'triangle'
    elif pen_select == 2: # square
        if draw_select == 0:
            label_text = 'thick'
        else: 
            label_text = 'square'
    label_id = canvas.create_text(550, 25, anchor=tk.SW, text=label_text, font=('Times', '12'), fill='#888')
    status_label_list[1] = (label_id)

    if color_select == 0: #red
        label_text = 'red'
    elif color_select == 1: #green
        label_text = 'green'
    elif color_select == 2: #blue
        label_text = 'blue'
    elif color_select >= 4: #eraser
        label_text = bgcolor
    label_id = canvas.create_text(550, 45, anchor=tk.SW, text=label_text, font=('Times', '12'), fill=label_text)
    status_label_list[2] = (label_id)
        

def canvas_draw_rectangle(left, top, right, bottom):
    global canvas
    global menu_list
    menu_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom,fill="white", outline='#aaa', width=3)
    menu_list.append([menu_id])

def canvas_draw_pen_option(pen, left, top, right, bottom):
    global canvas
    global menu_list
    option_id = 0
    if pen == "thin":
#        option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="blue", outline='#aaa', width=3)
        option_id = canvas.create_bitmap(left+2, top+2, anchor=tk.NW, bitmap="gray25")
        menu_list[-1].append(option_id)
    elif pen == "medium":
#        option_id = canvas.create_polygon(left+2, top+2, anchor=tk.NW, right, top, right, bottom, left, bottom, bitmap="gray50", outline='#aaa', width=3)
        option_id = canvas.create_bitmap(left+2, top+2, anchor=tk.NW, bitmap="gray50")
        menu_list[-1].append(option_id)
    elif pen == "thick":
#        option_id = canvas.create_polygon(left+2, top+2, anchor=tk.NW, right, top, right, bottom, left, bottom, bitmap="gray25", outline='#aaa', width=3)
        option_id = canvas.create_bitmap(left+2, top+2, anchor=tk.NW, bitmap="gray75")
        menu_list[-1].append(option_id)
        
def canvas_draw_color_option(color, left, top, right, bottom):
    global canvas
    global menu_list
    option_id = 0
    if color == "red":
        option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="red", outline='#aaa', width=3)
        menu_list[-1].append(option_id)
    elif color == "green":
        option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="green", outline='#aaa', width=3)
        menu_list[-1].append(option_id)
    elif color == "blue":
        option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="blue", outline='#aaa', width=3)
        menu_list[-1].append(option_id)

def canvas_draw_draw_switch(left, top, right, bottom):
        #option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="#e2c", outline='#aaa', width=3)
        option_id = canvas.create_bitmap(left, top+2, anchor=tk.NW, bitmap="gray12")
        menu_list[-1].append(option_id)
        option_id = canvas.create_bitmap(left+option_square_size, top+2, anchor=tk.NW, bitmap="error")
        menu_list[-1].append(option_id)

def canvas_draw_eraser(left, top, right, bottom):
    option_id = canvas.create_bitmap(left, top, anchor=tk.NW, bitmap="gray12")
    menu_list[-1].append(option_id)
    option_id = canvas.create_bitmap(left, top + option_square_size, anchor=tk.NW, bitmap="gray25")
    menu_list[-1].append(option_id)
    option_id = canvas.create_bitmap(left, top + 2 * option_square_size, anchor=tk.NW, bitmap="gray25")
    menu_list[-1].append(option_id)
    
def draw_menu(mouse_e):
    global canvas
    global option_square_size
    global pen_list, color_list
    global menu_area
    menu_height = max(len(pen_list),len(color_list))*option_square_size + 4 * option_square_size #the last one is draw select switch and eraser
    menu_width = 2*option_square_size 
    menu_area[2] = menu_width
    menu_area[3] = menu_height
    print menu_height, menu_width
    canvas_draw_rectangle(mouse_e.x, mouse_e.y, mouse_e.x+menu_width, mouse_e.y+menu_height)
    i = 0
    for pen_type in pen_list:
        canvas_draw_pen_option(pen_type, mouse_e.x, mouse_e.y + i*option_square_size, mouse_e.x + option_square_size, mouse_e.y + (i+1)*option_square_size)
        i += 1 
    i = 0
    for color in color_list:
        canvas_draw_color_option(color, mouse_e.x + option_square_size, mouse_e.y + i*option_square_size, mouse_e.x + 2*option_square_size, mouse_e.y + (i+1)*option_square_size)
        i += 1

    switch_Y = mouse_e.y + max(len(pen_list), len(color_list))*option_square_size   
    canvas_draw_draw_switch(mouse_e.x, switch_Y, mouse_e.x + 2*option_square_size, switch_Y + option_square_size)

    canvas_draw_eraser(mouse_e.x, switch_Y + option_square_size, mouse_e.x + 2 * option_square_size, switch_Y + 2*option_square_size)
    
    
def is_cursor_in_menu(cx, cy):
    global menu_area
    if menu_area[0] < cx < menu_area[0] + menu_area[2]:
        if menu_area[1] < cy < menu_area[1] + menu_area[3]:
            print "in menu"
            return True
    print "not in menu"
    return False
    
def select_option(cx, cy):
    global menu_area
    global option_square_size
    global draw_select, pen_select, color_select
    global no_draw

    no_draw = True
    pen_or_color = (cx - menu_area[0]) / option_square_size #0 is  pen, 1 is color
    selected_option = (cy - menu_area[1]) / option_square_size

    if color_select >= 4:
        color_select -= 4    

    if selected_option < 3:        
        if pen_or_color == 0: # pen
            pen_select = selected_option # 0: thin; 1:medium; 2:thick

        elif pen_or_color == 1:  #color
            color_select = selected_option #0: red; 1:green; 2: blue
    
    elif selected_option == 3: #draw switch
        if pen_or_color == 0:
            draw_select = 0
        else:
            draw_select = 1

    elif selected_option >= 4: #draw eraser
        if pen_or_color == 0:
            eraser_select = selected_option - 4
            draw_select = 0 # eraser is in fact a draw-line mode
            pen_select = eraser_select
            color_select += 4

    print "pen", pen_select, 'color', color_select, 'draw', draw_select            

    
def clear_menus(mouse_e):
    global canvas
    if len(menu_list) != 0:
        for menu in menu_list:
            for option in menu:
                canvas.delete(option)
            for option in menu:
                menu.remove(option)
            menu_list.remove(menu)
        return
    
def draw_dots(mouse_e):
    global canvas
    global radius
    global pen_select, color_select
    x = mouse_e.x
    y = mouse_e.y
    print x,y
    if pen_select == 0: #circle
        if color_select == 0:
            canvas.create_oval(x-circle_radius, y-circle_radius, x+circle_radius, y+circle_radius, fill='red', outline='red')
        elif color_select == 1:
            canvas.create_oval(x-circle_radius, y-circle_radius, x+circle_radius, y+circle_radius, fill='green', outline='green')
        elif color_select == 2:
            canvas.create_oval(x-circle_radius, y-circle_radius, x+circle_radius, y+circle_radius, fill='blue', outline='blue')
    elif pen_select == 1: # striganle
        if color_select == 0:
            canvas.create_polygon(x, y-1.712/3*10, x+10/2, y+1.712/6*10, x-10/2, y+1.712/6*10, fill='red', outline='red')
        if color_select == 1:
            canvas.create_polygon(x, y-1.712/3*10, x+10/2, y+1.712/6*10, x-10/2, y+1.712/6*10, fill='green', outline='green')
        if color_select == 2:
            canvas.create_polygon(x, y-1.712/3*10, x+10/2, y+1.712/6*10, x-10/2, y+1.712/6*10, fill='blue', outline='blue')
    elif pen_select == 2: # square
        if color_select == 0:
            canvas.create_polygon(x-10/2, y-10/2, x+10/2, y-10/2, x+10/2, y+10/2, x-10/2, y+10/2, fill='red', outline='red')
        if color_select == 1:
            canvas.create_polygon(x-10/2, y-10/2, x+10/2, y-10/2, x+10/2, y+10/2, x-10/2, y+10/2, fill='green', outline='green')
        if color_select == 2:
            canvas.create_polygon(x-10/2, y-10/2, x+10/2, y-10/2, x+10/2, y+10/2, x-10/2, y+10/2, fill='blue', outline='blue')

def drawing(mouse_e):
    global canvas
    global oldx, oldy
    global pen_select, color_select

    if oldx != 0 and oldy != 0:
        if color_select == 0:
            if pen_select == 0:  #thin
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill="red", width=1)
            if pen_select == 1:  #medicore
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill="red", width=3)
            if pen_select == 2:  #thick
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill="red", width=5)
        elif color_select == 1:
            if pen_select == 0:  #thin
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill="green", width=1)
            if pen_select == 1:  #medicore
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill="green", width=3)
            if pen_select == 2:  #thick
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill="green", width=5)
        elif color_select == 2:
            if pen_select == 0:  #thin
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill="blue", width=1)
            if pen_select == 1:  #medicore
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill="blue", width=3)
            if pen_select == 2:  #thick
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill="blue", width=5)
        elif color_select >= 4: # this is a eraser
            if pen_select == 0:  #thin
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill=bgcolor, width=1)
            if pen_select == 1:  #medicore
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill=bgcolor, width=3)
            if pen_select == 2:  #thick
                    canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y, fill=bgcolor, width=5)

    oldx = mouse_e.x
    oldy = mouse_e.y

##
## define handlers
##
def mouse1_down(mouse_e):
    global menu_is_showing
    if menu_is_showing:
        if is_cursor_in_menu(mouse_e.x, mouse_e.y):
            select_option(mouse_e.x, mouse_e.y)
            update_status_label()
            menu_is_showing = 0
            clear_menus(mouse_e)
            return
        else:
            menu_is_showing = 0
            clear_menus(mouse_e)
    if draw_select == 0: # lines
        canvas.bind('<Motion>', drawing)
#        draw_lines(mouse_e)

#    elif draw_select == 1: # dots
#        draw_dots(mouse_e)
#    canvas.after(100, mouse_click, mouse_e)
def mouse3_down(mouse_e):
    global menu_is_showing
    menu_is_showing = 0
    clear_menus(mouse_e)

def mouse1_up(mouse_e):
    if draw_select == 0: # lines
        global oldx, oldy
        oldx = 0
        oldy = 0
        canvas.unbind('<Motion>')
    else:
        global no_draw
        if no_draw:
            no_draw = False
        else:
            draw_dots(mouse_e)

def mouse3_up(mouse_e):
    global menu_is_showing
    global menu_area
    menu_is_showing = 1
    draw_menu(mouse_e)
    menu_area[0] = mouse_e.x
    menu_area[1] = mouse_e.y

## define window
root = tk.Tk()
root.title("SimpleDraw")
root.geometry("610x500+200+150")

canvas = tk.Canvas(root, width=610, height=500, bd=2, bg=bgcolor)
canvas.grid(column=0, row=0, columnspan=1, rowspan=1)

canvas.create_text(10,  25, anchor=tk.SW, text="draw status:", font=('Times', '12'), fill='#888')
label_id = canvas.create_text(90, 25, anchor=tk.SW, text="line", font=('Times', '12'), fill='#888')
status_label_list.append(label_id)
canvas.create_text(505, 25, anchor=tk.SW, text="pen   :", font=('Times', '12'), fill='#888')
label_id = canvas.create_text(550, 25, anchor=tk.SW, text="thin", font=('Times', '12'), fill='#888')
status_label_list.append(label_id)
canvas.create_text(505, 45, anchor=tk.SW, text="color :", font=('Times', '12'), fill='#888')
label_id = canvas.create_text(550, 45, anchor=tk.SW, text="red", font=('Times', '12'), fill='red')
status_label_list.append(label_id)

canvas.bind('<Button-1>', mouse1_down)
canvas.bind('<ButtonRelease-1>', mouse1_up)
canvas.bind('<Button-3>', mouse3_down)
canvas.bind('<ButtonRelease-3>', mouse3_up)

tk.mainloop()
