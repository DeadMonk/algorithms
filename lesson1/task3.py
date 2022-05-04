# -*- coding: utf-8 -*-
# !/usr/bin/python3
"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""

print(f'Введите координаты точек (x1, y1) и (x2, y2)')
x1 = int(input(f'x1 = '))
y1 = int(input(f'y1 = '))
x2 = int(input(f'x2 = '))
y2 = int(input(f'y2 = '))
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1
print(f'y={k}x+{b}')
