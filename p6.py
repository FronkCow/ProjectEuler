# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum_x = 0
sum_sq_x = 0
for x in range(1, 101):
    sum_x += x
    sum_sq_x += x * x
print(sum_x * sum_x - sum_sq_x)
