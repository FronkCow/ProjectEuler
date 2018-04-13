# https://projecteuler.net/problem=12
import math
over_fivehundred = False
counter = 0
curr_value = 0

while not over_fivehundred:
    curr_value += counter
    multiples_list = [curr_value]
    #print curr_value
    for x in range(1, int(curr_value / 2) + 1):
        if curr_value % x == 0:
            multiples_list.append(x)
    #print (multiples_list)
    if len(multiples_list) > 500:
        over_fivehundred = True
        print len(multiples_list)
    
    counter += 1