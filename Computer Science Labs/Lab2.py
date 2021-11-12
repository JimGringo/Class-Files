import math
from os import system
cls = lambda: system('cls')

print("Begin Test One")
hours = int(input("Enter Hours "))
minutes = int(input("Enter Minutes "))
seconds = int(input("Enter Seconds "))
totalSeconds = hours * 3600 + minutes * 60 + seconds
print(totalSeconds, 'Seconds')
next = input("Hit Enter to continue")

print("\nBegin Test Two")
seconds2 = int(input('Enter Seconds '))
hours2 = seconds2 // 3600
minutes2 = (seconds2 - hours2 * 3600) // 60
seconds2 = seconds2 % 60   
print(hours2, "Hours,", minutes2, "Minutes, and", seconds2, "Seconds")
next = input("Hit Enter to continue")

print("\nBegin Test Three")
quarters = 25 * int(input("Enter Quarters "))
dimes = 10 * int(input("Enter Dimes "))
nickels = 5 * int(input("Enter Nickels "))
pennies = 1 * int(input("Enter Pennies "))
totalCents = (quarters + dimes + nickels + pennies) / 100
print("This is equal to $", totalCents, sep="")
next = input("Hit Enter to continue")

print("\nBegin Test Four")
num1 = int(input("Enter Value 1 "))
num2 = int(input("Enter Value 2 "))
num3 = int(input("Enter Value 3 "))
num4 = int(input("Enter Value 4 "))
sum1 = num1 + num2 + num3 + num4
prod1 = sum1 / 4
print("Sum of Values:", sum1)
print("Average of Values:", prod1)
print("Value 1", num1, 'Difference:', math.fabs(prod1 - num1))
print("Value 2", num2, 'Difference:', math.fabs(prod1 - num2))
print("Value 3", num3, 'Difference:', math.fabs(prod1 - num3))
print("Value 4", num4, 'Difference:', math.fabs(prod1 - num4))

