#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Система рисования различных фракталов на Python
Copyright (c) 2023 Okulus Dev
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
import textwrap
import argparse
from fractals.dragon_curve import draw_dragon_curve
from fractals.fractals import draw_fractal


"""
Снежинка Коха

axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 4 # TOP: 7
angle = 60


Квадратный остров Коха

axiom = "F+F+F+F"
rules = {"F":"F-F+F+FFF-F-F+F"}
iterations = 2 # TOP: 4
angle = 90


Кристалл

axiom = "F+F+F+F"
rules = {"F":"FF+F++F+F"}
iterations = 3 # TOP: 6
angle = 90


Квадратная снежинка

axiom = "F--F"
rules = {"F":"F-F+F+F-F"}
iterations = 4 # TOP: 6
angle = 90


Фрактал Вичека

axiom = "F-F-F-F"
rules = {"F":"F-F+F+F-F"}
iterations = 4 # TOP: 6
angle = 90


Кривая Леви

axiom = "F"
rules = {"F":"+F--F+"}
iterations = 10 # TOP: 16
angle = 45


Ковер Серпинского

axiom = "YF"
rules = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
iterations = 1 # TOP: 10
angle = 60


Решетка Серпинского

axiom = "FXF--FF--FF"
rules = {"F":"FF", "X":"--FXF++FXF++FXF--"}
iterations = 7 # TOP: 8
angle = 60


Квадрат

axiom = "F+F+F+F"
rules = {"F":"FF+F+F+F+FF"}
iterations = 3 # TOP: 5
angle = 90


Плитки

axiom = "F+F+F+F"
rules = {"F":"FF+F-F+F+FF"}
iterations = 3 # TOP: 4
angle = 90


Кольца

axiom = "F+F+F+F"
rules = {"F":"FF+F+F+F+F+F-F"}
iterations = 2 # TOP: 4
angle = 90


Крест-2

axiom = "F+F+F+F"
rules = {"F":"F+F-F+F+F"}
iterations = 3 # TOP: 6
angle = 90


Pentaplexity

axiom = "F++F++F++F++F"
rules = {"F":"F++F++F+++++F-F++F"}
iterations = 1 # TOP: 5
angle = 36


32-сегментная кривая

axiom = "F+F+F+F"
rules = {"F":"-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"}
iterations = 3 # TOP: 3
angle = 90


Кривая Пеано-Госпера

axiom = "FX"
rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
iterations = 4 # TOP: 6
angle = 60


Кривая Серпинского

axiom = "F+XF+F+XF"
rules = {"X":"XF-F+F-XF+F+XF-F+F-X"}
iterations = 4 # TOP: 8
angle = 90


Анклеты Кришны

axiom = " -X--X"
rules = {"X":"XFX--XFX"}
iterations = 3 # TOP: 9
angle = 45


Квадратный фрактал Госпера

axiom = "YF"
rules = {"X": "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-", 
        "Y": "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"}
iterations = 2 # TOP: 3
angle = 90


Кривая Мура

axiom = "LFL-F-LFL"
rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
iterations = 0 # TOP: 8
angle = 90


Кривая Гильберта

axiom = "L"
rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
iterations = 8 # TOP: 9
angle = 90


Кривая Гильберта-II

axiom = "X"
rules = {"X":"XFYFX+F+YFXFY-F-XFYFX", "Y":"YFXFY-F-XFYFX+F+YFXFY"}
iterations = 4 # TOP: 6
angle = 90


Кривая Пеано

axiom = "F"
rules = {"F":"F+F-F-F-F+F+F+F-F"}
iterations = 2 # TOP: 5
angle = 90


Крест

axiom = "F+F+F+F"
rules = {"F":"F+FF++F+F"}
iterations = 3 # TOP: 6
angle = 90


Треугольник

axiom = "F+F+F"
rules = {"F":"F-F+F"}
iterations = 2 # TOP: 9
angle = 120


Кривая дракона

axiom = "FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 8 # TOP: 16
angle = 90


Кривая Terdragon

axiom = "F"
rules = {"F":"F-F+F"}
iterations = 5 # TOP: 10
angle = 120


Двойная кривая дракона

axiom = "FX+FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 6 # TOP: 16
angle = 90


Тройная кривая дракона

axiom = "FX+FX+FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 7 # TOP: 15
angle = 90"""


def main():
	parser = argparse.ArgumentParser(description='FractalIO', formatter_class=argparse.RawDescriptionHelpFormatter, 
								epilog=textwrap.dedent('''
Примеры использования:

// Кривая дракона
fractalio.py -dc
	'''))

	parser.add_argument('-dc', '--dragoncurve', action='store_true',
						help='Фрактал "Кривая дракона"')
	parser.add_argument('-t', '--triangle', action='store_true')

	args = parser.parse_args()

	if args:
		if args.dragoncurve:
			draw_dragon_curve()
		elif args.triangle:
			axiom = "F+F+F"
			rules = {"F":"F-F+F"}
			iterations = 9 # TOP: 9
			angle = 120
			draw_fractal(iterations, axiom, rules, angle)
	else:
		print('Вы не задали ни одного аргумента. --help для просмотра справки')


if __name__ == '__main__':
	main()
