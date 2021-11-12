userInt = int(input("Enter a value "))
sum = 0
negsum = 0
count1 = 0
count2 = 0
while True:
    if userInt == 0:
        break
    elif userInt > 0:
        sum += userInt
        count1 += 1
    elif userInt < 0:
        negsum += userInt
        count2 += 1
    userInt = int(input("Enter a value "))
if count1 > 0:
    print("Average of positive values:", format(sum/count1, '1.2f'))
if count2 > 0:
    print("Average of negative values:", format(negsum/count2, '1.2f'))


    
        