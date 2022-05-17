# -*- coding: utf-8 -*-
#!/usr/bin/python3

from random import randint

int_list = []
for i in range(randint(20, 50)):
    int_list.append(randint(0, 10))

res_dict = dict()
for i in int_list:
    if i in res_dict:
        res_dict[i] += 1
    else:
        res_dict[i] = 1

max_item = None
count = 1
for key, item in res_dict.items():
    if item > count:
        count = item
        max_item = key

print(res_dict)
print(f'Число {max_item} встречается {res_dict[max_item]} раз')
