from operator import itemgetter

# f = open("Day1/testData.txt", "r")
f = open("Day1/adventofcode.com_2023_day_1_input.txt", "r")
output = 0
numWordAry = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)
numAry = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


def FindFirstNumberWord(string):
    listOfWords = list()
    for i in range(1, 10):
        index = string.find(numWordAry[i])
        if index != -1:
            listOfWords.append({"number": i, "index": index})
    if len(listOfWords) != 0:
        # print(listOfWords)
        newList = sorted(listOfWords, key=itemgetter("index"))
        print(newList)
        return int(newList[0]["number"])
    else:
        return -1


def FixIncorrectUsageOfWords(string):
    string = string.replace("oneight", "oneeight")
    string = string.replace("threeight", "threeeight")
    string = string.replace("fiveight", "fiveeight")
    string = string.replace("nineight", "nineeight")
    string = string.replace("twone", "twoone")
    string = string.replace("sevenine", "sevennine")
    string = string.replace("eightwo", "eighttwo")
    return string


for x in f:
    print(x)
    x = FixIncorrectUsageOfWords(x)
    firstNumberWord = FindFirstNumberWord(x)
    escape = 0
    while firstNumberWord != -1:
        x = x.replace(numWordAry[firstNumberWord], str(firstNumberWord), 1)
        firstNumberWord = FindFirstNumberWord(x)
        if escape > 100:
            break
        else:
            escape += 1

    print(x)
    value1 = 0
    value2 = 0
    y = x[::-1]
    for char in x:
        # print(char)
        if char in numAry:
            value1 = char
            break
    for char in y:
        # print(char)
        if char in numAry:
            value2 = char
            break
    value = (int)(value1 + value2)
    print(value)
    output += value
print(output)
