fileName = input("Enter File Name ")
outFile = open(fileName, "w")

artist = input("Enter Song Artist ")
while artist != "":
    song = input("Enter Song Name ")
    time = input("Enter Length of song ")
    fileLine = artist + "-" + song + ":" + time
    outFile.write(fileLine)
    outFile.write("\n")
    artist = input("Enter Song Artist ")
