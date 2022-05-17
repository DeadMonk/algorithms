# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
 (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа."""

from random import randint

int_list = []
for i in range(randint(10, 100)):
    int_list.append(randint(0, 1000))

id_list = []
for id, val in enumerate(int_list):
    if val % 2 == 0:
        id_list.append(id)


print(int_list)
print(id_list)