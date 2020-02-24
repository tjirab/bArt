import random
from turtle import *
import turtle
import time
import json
import numpy as np
# from Tkinter import *

ts = turtle.getscreen()

# Config
hideturtle()
speed(0)
colormode(255)
canvas = ts.getcanvas()
height = ts.getcanvas()._canvas.winfo_height()
width = ts.getcanvas()._canvas.winfo_width()

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

def square(s):
	for i in range(4):
		right(90)
		forward(s)

def triangle(s):
	for i in range(3):
		right(120)
		forward(s)

# e = edges; s = size
def shape(e, s, random_angle=False):
	angle = 360 / e
	for i in range (e-1):
		if random_angle == True:
			angle = random.randint(round(angle * 0.2), round(angle * 5))
		right(angle)
		# forward(s)
		forward(5)


# If angle_random=True, n will be overwritten
def rotate(n, angle_random=False, direction_random=False):
	if angle_random == True:
		n = random.randint(0,360)
	if direction_random == True:
		direction = random.randint(0,1)
		if direction == 0:
			left(n)
		else:
			right(n)
	else:
		right(n)


def get_config():
	shapes = ['square', 'triangle', 'random']
	config = {}
	config['forward_val'] = random.randint(0,100)
	config['shape_type'] = random.choice(shapes)
	config['shape_size'] = random.randint(5, 25)
	config['shape_edges'] = random.randint(3,15) # only used when shape='random' 
	config['iterations'] = random.randint(5, 100)
	config['rotate_val'] = random.randint(1, 90)
	config['rotate_random_angle'] = bool(random.getrandbits(1))
	config['rodate_random_direction'] = bool(random.getrandbits(1))
	config['pen_color'] = tuple(np.random.choice(range(256), size=3))
	# TODO: behaviour: connect, jump, copy?
	print(json.dumps(config, cls=NpEncoder, indent=2, sort_keys=True))
	return config

def get_drawing():
	config = get_config()
	bgcolor("black")
	pencolor(config['pen_color'])

	for i in range(config['iterations']):

		forward(config['forward_val'])
		if config['shape_type'] == 'square':
			square(config['shape_size'])
		elif config['shape_type'] == 'triangle':
			triangle(config['shape_size'])
		elif config['shape_type'] == 'random':
			shape(config['shape_edges'], config['shape_size'], True)

		rotate(config['rotate_val'], config['rotate_random_angle'], config['rodate_random_direction'])

get_drawing()


# end_fill()

# Save and pass on params
# TODO: pass on parameters
ts.getcanvas().postscript(file="drawings/bart_{}.eps".format(round(time.time())))
# ts.getscreen().getcanvas().postscript(file="bart_test.ps")