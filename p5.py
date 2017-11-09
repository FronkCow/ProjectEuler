# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# smallest grouping of numbers that can produce every number from 1 - 10

# needs to be this way to be inclusive of 20
max_range_num = 20 + 1;

# start from 2 since every number is divisble by 1
cur_num = 2
for x in range(2, max_range_num):
    y = 2
    stack = []
    # create stack filled with multiples of x to test against cur_num
    while y <= x:
        if x % y == 0:
            stack.append(y)
            x = x / y
        else:
            y += 1
    # we do not want to override the cur_num
    test_num = cur_num
    # loop through test_num finding if there is a multiple of x that fails to
    # divide in
    while len(stack) != 0:
        stack_var = stack.pop()
        if test_num % stack_var != 0:
            # if it does fail, multiple cur_num by the multiple
            cur_num *= stack_var
        else:
            # if it does not fail, continue testing other multiples
            test_num /= stack_var
print(cur_num)
