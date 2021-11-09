def main():
    fileName = input("Enter File Name ")
    outFile = open(fileName, "w")
    score = 0
    while True:
        if score == -1:
            break
        score = int(input("Enter Score 0-100 or enter -1 to exit"))
        if 0 <= score <= 100:
            outFile.write(str(score))
            outFile.write("\n")
    outFile.close()
main()