# What is the 10 001st prime number?
import sys
import math

# maybe too big lol
# max_num = sys.maxsize
# print(max_num)

arb_limit = 200000000

list_all = [True] * arb_limit
list_prime = []

for x in range(2, int(math.sqrt(len(list_all)))):
    if list_all[x] == True:
        for y in range(x * x, len(list_all), x):
            list_all[y] = False
            list_prime.append(y)

print(list_prime)
