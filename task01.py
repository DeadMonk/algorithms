# -*- coding: utf-8 -*-
#!/usr/bin/python3

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

