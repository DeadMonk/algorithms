# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения."""
from random import randint

int_list = []
for i in range(randint(10, 20)):
    int_list.append(randint(-100, 100))

max_neg = None
for i in int_list:
    if i < 0 and max_neg is None or i < 0 and max_neg < i:
        max_neg = i

print(int_list)
print(max_neg)