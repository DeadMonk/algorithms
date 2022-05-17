# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

start_r = 2
end_r = 99
start_div = 2
end_div = 9

res = dict()
for i in range(start_div, end_div + 1):
    counter = 0
    for j in range(start_r, end_r + 1):
        if j % i == 0:
            counter += 1
    res[i] = counter

print(res)

