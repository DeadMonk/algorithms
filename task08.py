# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
 Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
  В конце следует вывести полученную матрицу."""

lc = 4
ec = 5
matrix = []
for ln in range(lc):
    lv = 0
    ml = []
    for le in range(ec - 1):
        val = int(input(f'Введите {le + 1} элемент строки {ln + 1}: '))
        lv += val
        ml.append(val)
    ml.append(lv)
    matrix.append(ml)

for l in matrix:
    print(l, end='\n')