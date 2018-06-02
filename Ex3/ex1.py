#!/usr/bin/env python3.6

list = [17,1,12,54,23,9,21]
j = 0
for i in list:
    if i >= 3 and i <=20:
        j += int(i)

print("I like to print stuff, sum of numbers between 3-20 in list is: {}".format(j))
