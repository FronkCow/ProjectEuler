# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

cur_palin = 0
for x in range(100, 999):
    for y in range(100, 999):
        z = x * y
        if str(z) == str(z)[::-1]:
            if z > cur_palin:
                cur_palin = z
print cur_palin
            
