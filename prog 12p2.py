def readSongs (fileName):
    songDict = {}
    inFile = open(fileName, "r")
    for line in inFile:
        song, min, sec = line.strip().split(":")
        time = min + ":" + sec
        songDict[song] = time
    return songDict


def totalSongs(musicInfo):
    length = len(musicInfo)
    return len

def updateSong (musicInfo, songToFind, newTime):
    if songToFind in musicInfo:
        musicInfo[songToFind] = newTime
        return True

def totalTime(musicInfo):
    totalSec = 0
    for item in musicInfo:
        min, sec = musicInfo[item].split(":")
        newSec = int(min)*60+int(sec)
        totalSec += newSec
    backToMin = totalSec//60
    backToSec = totalSec%60
    bigTime = str(backToMin) + ":" + str(backToSec)
    return bigTime

def findShortestSong(musicInfo):
    lowestTime = 10000
    for item in musicInfo:
        min, sec = musicInfo[item].split(":")
        possibleLow = int(min)*60+int(sec)
        if possibleLow < lowestTime:
            lowestTime = possibleLow
            song = item
    return song


def findLongestSong(musicInfo):
    longestTime = 0
    for item in musicInfo:
        min, sec = musicInfo[item].split(":")
        possibleHigh = int(min)*60+int(sec)
        if possibleHigh > longestTime:
            longestTime = possibleHigh
            song = item
    return song

def getSongTime(musicInfo, songToFind):
    if songToFind in musicInfo:
        return musicInfo[songToFind]
    return ""

def printMusic(musicInfo):
    print(format("Song / Artist", "<20s") + format("Time", ">10s"))
    for item in musicInfo:
        print(format(item, "<20s") + format(musicInfo[item], ">10s"))

def matchingSongs (musicInfo, textToFind):
    found = []
    for item in musicInfo:
        if item.find(textToFind) != -1:
            found.append(item)
    return found



def main():
    fileName = input("Enter File Name ")
    totalSongs(readSongs(fileName))
    updateSong (readSongs(fileName), "Chumbo-Bananas", "5:64")
    totalTime (readSongs(fileName))
    findShortestSong(readSongs(fileName))
    findLongestSong(readSongs(fileName))
    getSongTime(readSongs(fileName), "Chumbo-Bananas")
    printMusic(readSongs(fileName))
    matchingSongs(readSongs(fileName), "um")

main()