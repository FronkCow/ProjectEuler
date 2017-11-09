# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
giant_num = 600851475143
cur_num = 0

# for x in xrange(0, 600851475143 / 2):
    # if x % 2 != 0 and x % 3 != 0:
        # if giant_num % x == 0:
            # cur_num = x
x = 2
while x <= giant_num:
    if giant_num % x == 0:
        giant_num = giant_num / x
        cur_num = x
    x += 1
print(cur_num)
