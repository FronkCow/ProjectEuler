# What is the 10 001st prime number?
import sys
import math

# maybe too big lol
# max_num = sys.maxsize
# print(max_num)

#arb_limit = 200000000

#list_all = [True] * arb_limit

list_all = []
list_prime = []

print("part 2")

#upper_limit = int(math.sqrt(len(list_all)))

#counter = 0

#print(upper_limit)
#for x in xrange(2, arb_limit):
    #if (counter == 10001):
        #break
    #if list_all[x] == True:
        # logic here is  wrong, doesn't catch all primes
        #list_prime.append(x)
        #counter += 1
        #for y in xrange(x + x, len(list_all), x):
            #list_all[y] = False

#for x in xrange(2, arb_limit):
    #if list_all[x] == True:
        #list_prime.append(x)

arb_limit = 1000

all_count = 0
counter = 0
while counter != 10001:
    for x in range(0, 1000):
        list_all.append(True)
    for x in xrange(2, arb_limit):
        if list_all[all_count] == True:
            print(all_count)
            list_prime.append(all_count)
            counter += 1
            for y in xrange(all_count + x, all_count + arb_limit, x):
                list_all[y] = False
        all_count += 1
print(list_prime[10000])
