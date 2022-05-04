# -*- coding: utf-8 -*-
# !/usr/bin/python3
"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

sp = ord('a') - 1
letter1 = input(f'Введите буку от a до z: ')
letter2 = input(f'Введите буку от a до z: ')
l1p = ord(letter1) - sp
l2p = ord(letter2) - sp
ldiff = l2p - l1p
if ldiff < 0:
    ldiff *= -1
print(f'Позиция буквы {letter1} - {l1p}, Позиция буквы {letter2} - {l2p}, количество букв между ними {ldiff}')