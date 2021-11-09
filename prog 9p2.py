fileName = input("Enter File Name ")
outFile = open(fileName, "r")
teamStats = []
for line in outFile:
    teamStats.append(line.strip())

def displayTeam(data):
    for x in data:
        #print(data[x].split("|"))
        y, z = x.split("|")
        print(format(y, "20s") + z)

def findTotalTime(data):
    totalTime = 0
    for x in data:
        o, z = x.split("|")
        min, sec = z.split(":")
        min, sec = int(min), int(sec)
        totalTime += min * 60 + sec 
    min, sec = totalTime // 60, totalTime % 60
    newString = str(min) + ":" + str(sec)
    return newString

def getStudent(data, index):
    if index <= (len(data)-1):
        x, y = data[index].split("|")
        return x
    else:
        return ""

def getStudentTime(data, nameToFind):
    for x in data:
        y, z = x.split("|")
        if y == nameToFind:
            return z
    return ""

displayTeam(teamStats)
print("Total Team Time:", findTotalTime(teamStats))
index = int(input("Enter Student # to find "))
print("Name:", getStudent(teamStats, index))
name = input("Enter Student Name to Find their Time ")
print("Time for ", name, ": ", getStudentTime(teamStats, name), sep="")