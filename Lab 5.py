totalHonor = 0
totalCredits = 0
creditsPassed = 0
classesPassed = 0
totalClasses = 0
while True:
    className = input("Enter Class Name ")
    if className == "":
        break    
    credits = int(input("Enter Class Credit Value "))
    grade = input("Enter Class Grade ")
    if grade != 'f' and grade != 'F':
        creditsPassed += credits
        classesPassed += 1
    if  grade == "a" or grade == "A":
        totalHonor += credits * 4
        totalCredits += credits
    elif  grade == "b" or grade == "B":
        totalHonor += credits * 3
        totalCredits += credits
    elif  grade == "c" or grade == "C":
        totalHonor += credits * 2
        totalCredits += credits
    elif  grade == "d" or grade == "D":
        totalHonor += credits * 1
        totalCredits += credits    
    elif  grade == "f" or grade == "F":
        totalHonor += credits * 0
        totalCredits += credits 
    else:
        print("Invalid Letter Grade")
    totalClasses += 1
    print("")

gpa = totalHonor / totalCredits    
print("GPA:             ", format(gpa, "1.3f"))
print("Credits attempts     ", totalCredits)
print("Credits passed       ",creditsPassed)
print("Classes attempted    ",totalClasses)
print("Classes passed       ",classesPassed)
