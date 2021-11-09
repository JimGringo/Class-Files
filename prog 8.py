def main():
    fileName = input("Enter File Name to Read from ")
    myList = fillListFromFile(fileName)
    toFind = int(input("Select a Number to Find from the List "))
    print(findMax(myList))
    print(findMin(myList))
    print(calcRange(myList))
    print(calcAverage(myList))
    print(calcGeometicMean(myList))
    print(findFirst(myList, toFind))
    print(findLast(myList, toFind))
    print(findClosestValue(myList, toFind))
    print(calcCount(myList, toFind))
    print(isInList(myList, toFind))
def fillListFromFile(fileName):
    fileData = open(fileName, "r")
    myList = []
    for line in fileData:
        value = int(line.strip())
        myList.append(value)
    return myList
def findMax(myList):
    maxNum = 0
    for num in myList:
        if num > maxNum:
            maxNum = num
    return maxNum
def findMin(myList):
    minNum = 10000
    for num in myList:
        if num < minNum:
            minNum = num
    return minNum
def calcRange(myList):
    return (findMax(myList) - findMin(myList))
def calcAverage(myList):
    average = 0
    x = 0
    for num in myList:
        average += num
        x += 1
    return (average / x)
def calcGeometicMean(myList):
    geoMean = 1
    n = 0
    for num in myList:
        geoMean *= num
        n += 1
    return geoMean**(1/n)
def findFirst(myList, valueToFind):
    x = -1
    firstIndex = x
    for num in myList:
        x += 1
        if num == valueToFind:
            firstIndex = x
            return firstIndex
    return firstIndex
def findLast(myList, valueToFind):
    x = -1
    lastIndex = x
    for num in myList:
        x += 1
        if num == valueToFind:
            lastIndex = x
    return lastIndex          
def findClosestValue(myList, valueToFind):
    benchmark = 10000
    for num in myList:
        closeTo0 = abs(valueToFind - num)
        if closeTo0 < benchmark:
            benchmark = closeTo0
            marker = num
    return marker
def calcCount(myList, valueToFind):
    count = 0
    for num in myList:
        if num == valueToFind:
            count += 1
    return count
def isInList(myList, valueToFind):
    for num in myList:
        if num == valueToFind:
            return True
    return False
main()