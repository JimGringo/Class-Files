#Cody Nelson program 6
import os 
def main():
    minNum = 101
    maxNum = -1
    totalNum = 0
    loopsDone = 0
    ninetyPlus = 0
    notQuite90 = 0
    seventySent = 71
    underSeventy = 71
    #dataFile = "bingo.txt"
    dataFile = input("Enter text file ")
    inFile = open(dataFile, "r")    
    isEmpty = os.path.getsize(dataFile)
    if os.path.isfile(dataFile) == False:
        print("Not today Buddy")
    elif isEmpty == 0:
        print("No Data was found in this file")
    else:
        inFile = open(dataFile, "r")
        for num in inFile:
            num = int(num.strip())
            seventyPlus = 70 - num
            totalNum += num
            loopsDone += 1
            if maxNum < num:
                maxNum = num
            if minNum > num:
                minNum = num
            if num >= 90:
                ninetyPlus += 1
            else:
                notQuite90 += 1
            if abs(seventyPlus) < seventySent:
                seventySent = abs(seventyPlus)  #getting the seventies to work was a pain in my ass, easy fix but took a long time to find.
                seventySentP = num
            if (num <= 70) and (seventyPlus < underSeventy):
                underSeventy = seventyPlus
                underSeventyP = num
        print("Minimum Value",minNum)
        print("Maximum Value",maxNum)
        if maxNum == 100:
            print("100 was on the list")
        if minNum == 0:
            print("0 was on the list")
        print("Average Value", format(totalNum/loopsDone,"1.2f"))
        print("# of Values", loopsDone)
        print("Values 90 and above", ninetyPlus)
        print("Values below 90", notQuite90)
        print("Closest to 70", seventySentP)
        print("Closest to 70 but with a catch", underSeventyP)
    
main()