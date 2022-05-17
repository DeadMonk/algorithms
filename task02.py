# -*- coding: utf-8 -*-
#!/usr/bin/python3

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