def summation (intValue):
    sum1 = 0
    for x in range(intValue):
        sum1 += x+1
    return sum1
def square (intValue):
    return intValue**2
def sumOfSquare(intValue):
    sum = 0
    for x in range(intValue):
        sum += (x+1)**2
    return sum
def factorial(intValue):
    sum = 1
    for x in range(intValue):
        sum *= x+1
    return sum
def compare(intValue, intValue2):
    if intValue < intValue2:
        return -1
    elif intValue == intValue2:
        return 0
    else:
        return 1

def isOdd(intValue):
    if intValue % 2 != 0:
        return True
def isEven(intValue):
    if isOdd(intValue) == True:
        return False
    else:
        return True
intValue = int(input("Enter a Number "))
intValue2 = int(input("Enter 2nd Number "))
print(square(intValue))
print(summation(intValue))
print(sumOfSquare(intValue))
print(factorial(intValue))
print(compare(intValue, intValue2))
print(isOdd(intValue))
print(isEven(intValue))
