part = input("Enter a Part Name")
partList = {}
while part != "":
    price = input("Enter Price for this Part")
    partList[part] = price
    part = input("Enter a Part Name")

fileName = input("Enter File Name")
outFile = open(fileName, "w")

for key, value in partList:
    outFile.write(key + "\t" + value)
    outFile.write("\n")

outFile.close()
