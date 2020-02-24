import random
from turtle import *
import turtle
import time
# from Tkinter import *

ts = turtle.getscreen()
hideturtle()

# turtle.speed(10)
speed(0)
# color('blue', 'yellow')


# begin_fill()

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



# size = 200
# for i in range(8):
# 	square(size)
# 	size = size / 2.0

# shapes = ['square', 'triangle', 'random']
# shapes = ['random']
shapes = ['square']

# loop_range = random.randint(20,40)
loop_range = 20
print("INFO loop_range: {}".format(loop_range))
for i in range(random.randint(20,100)):
	forward_val = random.randint(0,100)
	# forward_val = 30
	shape_type = random.choice(shapes)
	shape_size = random.randint(5, 25)
	# shape_size = 200
	print("INFO forward_val: {}".format(forward_val))
	print("INFO shape_type: {}".format(shape_type))
	print("INFO shape_val: {}".format(shape_size))

	forward(forward_val)
	
	if shape_type == 'square':
		square(shape_size)
	elif shape_type == 'triangle':
		triangle(shape_size)
	elif shape_type == 'random':
		e = random.randint(3,15)
		shape(e, shape_size, True)

	rotate(10, True, False)
	print("-"*80)



# end_fill()

# Save and pass on params
# TODO: pass on parameters
ts.getcanvas().postscript(file="drawings/bart_{}.eps".format(round(time.time())))
# ts.getscreen().getcanvas().postscript(file="bart_test.ps")