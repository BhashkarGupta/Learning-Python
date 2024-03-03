with open("file3.txt", "w") as textFile:
    for x in range(50):
        temp = f"This is the line {x}\n"
        textFile.write(temp)