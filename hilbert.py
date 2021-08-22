import turtle
import math
import random

tut=turtle.Turtle()
tut.screen.bgcolor("black")
tut.screen.colormode(255)
tut.pencolor(255,255,255)

order=5
rotate=90
size=512
step_length=size/math.pow(2,order)
tut.penup()
tut.goto(-223,223)
tut.pendown()
tut.speed("fastest")

def hilbert(order,rotate,step_length):
	if order == 0:
		return 0
	tut.right(rotate)
	hilbert(order-1,-rotate,step_length)

	tut.forward(step_length)
	tut.left(rotate)
	hilbert(order-1,rotate,step_length)
	
	tut.forward(step_length)
	hilbert(order-1,rotate,step_length)

	tut.left(rotate)
	tut.forward(step_length)
	hilbert(order-1,-rotate,step_length)

	tut.right(rotate)


hilbert(order,rotate,step_length)

turtle.done()
