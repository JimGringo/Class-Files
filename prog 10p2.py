fileName = input("Enter FileName")

def readParts(fileName):
    inFile = open(fileName, "r")
    partPrice = {}
    for line in inFile:
        key, value = line.strip().split("\t")
        partPrice[key] = value
    return partPrice

def totalParts(theDictionary):
    x = 0
    for line in theDictionary:
        x += 1
    return x

def partsLessThan(theDictionary, upperLimit):
    cheapParts = []
    x = 0
    for key, values in theDictionary.items():
        if float(values) <= upperLimit:
            cheapParts.append(key)
    return cheapParts

def leastExpensivePart(theDictionary):
    baseline = 10000
    for item in theDictionary:
        if float(theDictionary[item]) <= baseline:
            baseline = float(theDictionary[item])
            newCheapest = item
    return newCheapest

def mostExpensivePart(theDictionary):
    baseline = 0
    for item in theDictionary:
        if float(theDictionary[item]) >= baseline:
            baseline = float(theDictionary[item])
            newBillGates = item
    return newBillGates

def averagePrice(theDictionary):
    average = 0
    x = 0
    for item in theDictionary:
        average += float(theDictionary[item])
        x += 1
    average = average / x
    return average

def printParts(theDictionary):
    partList = []
    for item in theDictionary:
        partList.append(item.capitalize())
    partList.sort()
    x = 0
    print(format("Part", "10s") + format("Price", ">10"))
    for key in theDictionary:
        print(format(partList[x], "10s") + format(format(float(theDictionary[key]), ".2f"), ">10"))
        x += 1


print("Total Parts", totalParts(readParts(fileName)))
print("Parts Less than 10 dollars", partsLessThan(readParts(fileName), 10))
print("Least expensive part", leastExpensivePart(readParts(fileName)))
print("MOst expensive part", mostExpensivePart(readParts(fileName)))
print("Average Price", averagePrice(readParts(fileName)))
printParts(readParts(fileName))