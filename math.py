import math
x = 1
bigMath = 0
while True:
    bigMath += math.atan(x+1)-math.atan(x)
    x += 1
    print(bigMath)