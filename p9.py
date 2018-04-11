# https://projecteuler.net/problem=9

a = 0 
b = 0
c = 1000

correctNum = 0
finished = False
for x in range(0, 1000):
    c = 1000 - x
    b = x
    a = 0
        
    for y in range(0, x):
        if (a + 1 < b):
            a = a + 1
            b = b - 1 

        if a * a + b * b == c * c and c > b and b > a:
            # print str(a) + ", " + str(b) + ", " + str(c) + ", " + str(a * a + b * b) + ", " + str(c * c)
            correctNum = a * b * c

print "The product of a * b * c is " + str(correctNum)