# https://projecteuler.net/problem=12
import math
over_fivehundred = False
counter = 0
curr_value = 0

while not over_fivehundred:
    curr_value += counter
    multiples_list = []
    # print curr_value
    for x in range(1, int(math.ceil(math.sqrt(curr_value)))):
        if curr_value % x == 0:
            multiples_list.append(curr_value / x)
            multiples_list.append(x)
    # print (multiples_list)
    if len(multiples_list) > 500:
        over_fivehundred = True
        print "final num: " + str(curr_value)
        print "final len: " + str(len(multiples_list))
    
    counter += 1