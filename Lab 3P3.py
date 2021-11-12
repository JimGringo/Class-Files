completeCred = int(input("Please Enter Your Current Number of Completed Credits "))
currentCred = int(input("How Many Credits are you Taking this Semester "))
totalCred = completeCred + currentCred
if completeCred >= 90:
    print("You are currently a Senior")
elif completeCred >= 60 and completeCred <= 89:
    print("You are currently a Junior")
elif completeCred >= 24 and completeCred <= 59:
    print("You are currently a Sophomore")
else:
    print("You are currently a Freshman")   

if totalCred >= 90:
    print("You will be a Senior after this semester")
elif totalCred >= 60 and totalCred <= 89:
    print("You will be a Junior after this semester")
elif totalCred >= 24 and totalCred <= 59:
    print("You will be a Sophomore after this semester")
else:
    print("You will be a Freshman after this semester") 

if totalCred >= 120:
    print("You have the required credits to graduate")
else:
    print("You will need", 120 - totalCred, "credits to graduate")

