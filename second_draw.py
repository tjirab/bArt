import random
from turtle import *
import turtle
import time
import json
import numpy as np
from tkinter import *

# Ideas:
# TODO: create pattern and "release" it into n different directions
# TODO: fill canvas with shape and build on top of existing shapes until canvas is filled
# TODO: possible to continue from vertices of a shape?
# TODO: stack lines
# TODO: dots to be connected
# TODO: first choose method, than geometry?


# Config
hideturtle()
speed(0)
colormode(255)

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


def draw_background(t):
	print("DEBUG draw_background - start")
	""" Draw a background rectangle. """
	ts = t.getscreen()
	canvas = ts.getcanvas()
	height = ts.getcanvas()._canvas.winfo_height()
	width = ts.getcanvas()._canvas.winfo_width()

	turtleheading = t.heading()
	turtlespeed = t.speed()
	penposn = t.position()
	penstate = t.pen()

	t.penup()
	t.speed(0)
	t.goto(-width/2-2, -height/2+3)
	t.fillcolor(turtle.Screen().bgcolor())
	t.begin_fill()
	t.setheading(0)
	t.forward(width)
	t.setheading(90)
	t.forward(height)
	t.setheading(180)
	t.forward(width)
	t.setheading(270)
	t.forward(height)
	t.end_fill()
	t.penup()
	t.setposition(*penposn)
	t.pen(penstate)
	t.setheading(turtleheading)
	t.speed(turtlespeed)


def square(s):
	for i in range(4):
		right(90)
		forward(s)

def triangle(s):
	for i in range(3):
		right(120)
		forward(s)

def draw_circle(s):
	circle(s)


# draw_complex_circle
# * s = size
# * n = amount of circles
def draw_complex_circle(s, n):
	angle = 360 / n
	for i in range(n):
		circle(s)
		right(angle)


# TODO: draw_parallelogram
def draw_parallelogram():
	return


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
	shapes = ['square', 'triangle', 'random', 'circle', 'complex_circle']
	config = {}
	config['forward_val'] = random.randint(0,100)
	config['shape_type'] = random.choice(shapes)
	config['shape_size'] = random.randint(5, 25)
	config['shape_edges'] = random.randint(3,15) # only used when shape='random' and for draw_complex_circle
	config['iterations'] = random.randint(50, 150)
	config['rotate_val'] = random.randint(1, 90)
	config['rotate_random_angle'] = bool(random.getrandbits(1))
	config['rotate_random_direction'] = bool(random.getrandbits(1))
	
	# determine theme
	white_bg = bool(random.getrandbits(1))
	if white_bg == True:
		config['bg_color'] = 'white'
		config['pen_color'] = 'black'
	else:
		config['bg_color'] = 'black'
		config['pen_color'] = tuple(np.random.choice(range(256), size=3))

	# TODO: behaviour: connect, jump, copy?
	print(json.dumps(config, cls=NpEncoder, indent=2, sort_keys=True))
	return config


def get_drawing(config):
	
	pencolor(config['pen_color'])

	for i in range(config['iterations']):

		forward(config['forward_val'])
		if config['shape_type'] == 'square':
			square(config['shape_size'])
		elif config['shape_type'] == 'triangle':
			triangle(config['shape_size'])
		elif config['shape_type'] == 'random':
			r = random.randint(1,5)
			if r == 1:
				square(config['shape_size'])
			elif r == 2:
				draw_circle(config['shape_size'])
			elif r == 3:
				triangle(config['shape_size'])
			elif r == 4:
				shape(config['shape_edges'], config['shape_size'], True)
			elif r == 5:
				draw_complex_circle(config['shape_size'], config['shape_edges'])
		elif config['shape_type'] == 'circle':
			draw_circle(config['shape_size'])
		elif config['shape_type'] == 'complex_circle':
			draw_complex_circle(config['shape_size'], config['shape_edges'])

		rotate(config['rotate_val'], config['rotate_random_angle'], config['rotate_random_direction'])


def main():
	print("DEBUG main - start")
	config = get_config()
	s = turtle.Screen()
	print("DEBUG main - config['bg_color']: {}".format(config['bg_color']))
	s.bgcolor(config['bg_color'])  # get from config
	t = turtle.Turtle()
	draw_background(t)
	ts = t.getscreen()
	canvas = ts.getcanvas()
	get_drawing(config)
	canvas.postscript(file="drawings/bart_{}.eps".format(round(time.time())))


if __name__ == '__main__':
	main()