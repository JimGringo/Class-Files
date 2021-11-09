year = int(input("Enter a Year from 2020 to 2029 "))
if year >= 2020 and year <= 2029:
    print(year, "is between 2020 and 2029")
else:
    print("Number is not in valid range")
    
creditsPassed = int(input("Enter how many credits you have passed "))
if creditsPassed >= 0 and creditsPassed <= 23:
    print("You are a Freshmen")
elif creditsPassed >= 24 and creditsPassed <= 59:
    print("You are a Sophomore")
elif creditsPassed >= 60 and creditsPassed <= 89:
    print("You are a Junior")
else:
    print("Your are a Senior")

gpa = float(input("Enter your GPA "))
if gpa >= 4.0:
    print("Your GPA is Excellent")
elif gpa >= 3.7:
    print("Your GPA is Very Good")
elif gpa >= 3.0:
    print("Your GPA is Good")
elif gpa >= 2.7:
    print("Your GPA is Above Average")
elif gpa >= 2.4:
    print("Your GPA is Average")
elif gpa >= 2.0:
    print("Your GPA is Satisfactory")
else:
    print("Your GPA SUCKS")
    
if gpa >= 2.2 and creditsPassed >= 120:
    print('You are Eligable to Graduate')
else:
    print('You do not meet graduation requirements')

integer = int(input("Enter an Integer that is divisible by 5 "))
if integer % 5 == 0:
    print(integer, "is a multiple of 5")
    if integer % 2 == 0:
        print(integer, "is also even")
    else:
        print(integer, "is also odd")
else:
    print(integer, "is not a multiple of 5")

int2 = int(input("Enter any integer in the 100s "))
if int2 >= 100 and int2 < 200:
    print(int2, "is a '100s' value")
else:
    print(int2, "is outside the '100s' range")

