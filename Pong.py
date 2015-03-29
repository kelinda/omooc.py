# Ball motion with an implicit timer

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0] # pixels per update (1/60 seconds)

# define event handlers
def draw(canvas):
    # judge boncing
    if ball_pos[0] + vel[0] < BALL_RADIUS or ball_pos[0] + vel[0] > WIDTH - BALL_RADIUS:
        vel[0] = -vel[0]
    if ball_pos[1] + vel[1] < BALL_RADIUS or ball_pos[1] + vel[1] > HEIGHT - BALL_RADIUS:
        vel[1] = -vel[1]
        
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# define key handlers
def key_up(key):
    if key == simplegui.KEY_MAP["left"]:
        vel[0] -=1
    elif key == simplegui.KEY_MAP["right"]:
        vel[0] += 1
    elif key == simplegui.KEY_MAP["up"]:
        vel[1] -= 1
    elif key == simplegui.KEY_MAP["down"]:
        vel[1] += 1
    
# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keyup_handler(key_up)

# start frame
frame.start()
