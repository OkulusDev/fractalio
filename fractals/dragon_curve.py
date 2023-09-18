#!/usr/bin/python3
# Кривая дракона
import turtle as tl


def dragon_curve(level, n):
	if (n == 13):
		return level
	
	newlevel = ''

	for i in level:
		if i == '+':
			newlevel += '+'
		elif i == '-':
			newlevel += '-'
		elif i == 'F':
			newlevel += 'F'
		elif i == 'X':
			newlevel += 'X+YF+'
		elif i == 'Y':
			newlevel += '-FX-Y'

	level = newlevel

	return dragon_curve(level, n + 1)

def draw_dragon_curve():
	way = dragon_curve('FX', 1)

	pen = tl.Turtle()
	pen.screen.title('Dragon Curve | FractalIO')

	tl.speed(1000000000)
	tl.penup()
	tl.setx(50)
	tl.sety(50)
	tl.pendown()

	for i in way:
		if i == '-':
			tl.left(90)
		elif i == '+':
			tl.right(90)
		else:
			tl.forward(3)
