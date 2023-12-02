# f = open("Day2/testData.txt", "r")
f = open("Day2/adventofcode.com_2023_day_2_input.txt", "r")

redLimit = 12
greenLimit = 13
blueLimit = 14


def checkForValidGame(cubeInput):
    for round in cubeInput:
        cubeList = round.split(",")
        for cube in cubeList:
            cubeDescription = cube.split(" ")
            print(cubeDescription)
            if "red" in cubeDescription[2]:
                if int(cubeDescription[1]) > redLimit:
                    return False

            elif "green" in cubeDescription[2]:
                if int(cubeDescription[1]) > greenLimit:
                    return False

            elif "blue" in cubeDescription[2]:
                if int(cubeDescription[1]) > blueLimit:
                    return False
    return True


def determinePowerOfCubes(cubeInput):
    redMin = 0
    greenMin = 0
    blueMin = 0
    for round in cubeInput:
        cubeList = round.split(",")
        for cube in cubeList:
            cubeDescription = cube.split(" ")
            print(cubeDescription)
            cubeCount = int(cubeDescription[1])
            if "red" in cubeDescription[2]:
                if cubeCount > redMin:
                    redMin = cubeCount

            elif "green" in cubeDescription[2]:
                if cubeCount > greenMin:
                    greenMin = cubeCount

            elif "blue" in cubeDescription[2]:
                if cubeCount > blueMin:
                    blueMin = cubeCount
    return redMin * greenMin * blueMin


def mainPart1():
    sumOfValidGameNumbers = 0
    for line in f:
        line = line.replace("\n", " ")
        gameNumber = int(line.split(":")[0].split(" ")[1])
        cubeInput = line.split(":")[1].split(";")
        print(gameNumber)
        print(cubeInput)
        gameValid = checkForValidGame(cubeInput)

        if gameValid:
            sumOfValidGameNumbers += gameNumber
    print(sumOfValidGameNumbers)


def mainPart2():
    sumOfGamePowers = 0
    for line in f:
        line = line.replace("\n", " ")
        gameNumber = int(line.split(":")[0].split(" ")[1])
        cubeInput = line.split(":")[1].split(";")
        print(gameNumber)
        print(cubeInput)
        sumOfGamePowers += determinePowerOfCubes(cubeInput)
    print(sumOfGamePowers)


# mainPart1()
mainPart2()
