# -*- coding: utf-8 -*-
# !/usr/bin/python3
"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

lnum = int(input(f'Введите номер буквы в диапазоне от 1 до 26: '))
sp = ord('a') - 1
letter = chr(sp + lnum)
print(f'{letter = }')