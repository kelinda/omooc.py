import Tkinter as tk

## define globals
draw_status = 0 #0 for lines, 1 for dots
pen_status = 0 #
color_status = 0 #

pen_list = ["triangle", "circle", "square"]
color_list = ["red", "green", "blue"]
menu_list = [[]] #menu_list ids, subsequence hold drawing-option icon ids.

option_square_size = 15  # drawing-option icon is square, this is the size.
circle_radius = 5 # circle dots radius
triangle_size = 10 # triangle dot side length
square_size = 10 # square dot side lenght

oldx = 0
oldy = 0

## define helpers
def canvas_draw_rectangle(left, top, right, bottom):
    global canvas
    global menu_list
    menu_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom,fill="white")
    menu_list.append([menu_id])

def canvas_draw_pen_option(pen, left, top, right, bottom):
    global canvas
    global menu_list
    option_id = 0
    if pen == "triangle":
        option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="blue")
        menu_list[-1].append(option_id)
    elif pen == "circle":
        option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="red")
        menu_list[-1].append(option_id)
    elif pen == "square":
        option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="green")
        menu_list[-1].append(option_id)
        
def canvas_draw_color_option(color, left, top, right, bottom):
    global canvas
    global menu_list
    option_id = 0
    if color == "red":
	    option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="red")
	    menu_list[-1].append(option_id)
    elif color == "green":
	    option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="green")
	    menu_list[-1].append(option_id)
    elif color == "blue":
	    option_id = canvas.create_polygon(left, top, right, top, right, bottom, left, bottom, fill="blue")
	    menu_list[-1].append(option_id)

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
	x = mouse_e.x
	y = mouse_e.y
	print x,y
	canvas.create_oval(x-circle_radius, y-circle_radius, x+circle_radius, y+circle_radius)

def drawing(mouse_e):
    global canvas
    global oldx, oldy
    if oldx != 0 and oldy != 0:
        canvas.create_line(oldx, oldy, mouse_e.x, mouse_e.y)
    oldx = mouse_e.x
    oldy = mouse_e.y

## define handlers
def mouse1_down(mouse_e):
    clear_menus(mouse_e)
    if draw_status == 0: # lines
        canvas.bind('<Motion>', drawing)
#        draw_lines(mouse_e)

#    elif draw_status == 1: # dots
#        draw_dots(mouse_e)
#    canvas.after(100, mouse_click, mouse_e)
def mouse3_down(mouse_e):
    clear_menus(mouse_e)

def mouse1_up(mouse_e):
    if draw_status == 0: # lines
        global oldx, oldy
        oldx = 0
        oldy = 0
        canvas.unbind('<Motion>')

    else:
        draw_dots(mouse_e)

def mouse3_up(mouse_e):
    global canvas
    global option_square_size
    global pen_list, color_list
    menu_height = max(len(pen_list),len(color_list))*option_square_size
    menu_width = 2*option_square_size 
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

## define window
root = tk.Tk()
root.title("simple palette")
root.geometry("600x500+200+150")

beginButton = tk.Button(root,text="begin",width=20, height=1)
beginButton.grid(column=0, row=0)
canvas = tk.Canvas(root, width=400, height=200, bd=20, bg="#EEE")
canvas.grid(column=1, row=0, columnspan=2, rowspan=2)
canvas.create_line(100, 10, 40, 5, 45, 20, fill = 'red', width = 2)
canvas.create_oval(100, 100, 200, 50 )
canvas.create_polygon(3,3, 100,120, 50,150, fill= "blue", activefill="red")

canvas.bind('<Button-1>', mouse1_down)
canvas.bind('<ButtonRelease-1>', mouse1_up)
canvas.bind('<Button-3>', mouse3_down)
canvas.bind('<ButtonRelease-3>', mouse3_up)

tk.mainloop()

