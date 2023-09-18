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


def main():
	parser = argparse.ArgumentParser(description='FractalIO', formatter_class=argparse.RawDescriptionHelpFormatter, 
								epilog=textwrap.dedent('''
Примеры использования:

// Кривая дракона
fractalio.py -dc
	'''))

	parser.add_argument('-dc', '--dragoncurve', action='store_true',
						help='Фрактал "Кривая дракона"')

	args = parser.parse_args()

	if args:
		if args.dragoncurve:
			draw_dragon_curve()
	else:
		print('Вы не задали ни одного аргумента. --help для просмотра справки')


if __name__ == '__main__':
	main()