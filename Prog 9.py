crossName = input("Enter Students Name ")
fileName = input("Enter File Name ")
inFile = open(fileName, "w")
while crossName != "":
    mostRun = input("Enter Students Best Time ")
    inFile.write(crossName)
    inFile.write("|")
    inFile.write(mostRun)
    inFile.write("\n")
    crossName = input("Enter Students Name ")