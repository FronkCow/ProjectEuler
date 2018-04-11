# https://projecteuler.net/problem=10
import sys
import math

# maybe too big lol
# max_num = sys.maxsize
# print(max_num)

arb_limit = 2000000

list_all = [True] * arb_limit
list_prime = []

print("part 2")

upper_limit = int(math.sqrt(len(list_all)))

print(upper_limit)
for x in xrange(2, upper_limit):
    if list_all[x] == True:
        # logic here is  wrong, doesn't catch all primes
        # list_prime.append(x)
        for y in xrange(x + x, len(list_all), x):
            list_all[y] = False

for x in xrange(2, arb_limit):
    if list_all[x] == True:
        list_prime.append(x)

sum_prime = sum(list_prime)

print(sum_prime)