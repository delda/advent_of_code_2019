from globalFunctions import readInputFile

def solvePart1():
    inp = readInputFile('../Resources/Day1Input')
    result = 0
    for line in inp:
        result += (int(int(line) / 3) - 2)
    print result

def solvePart2():
    inp = readInputFile('../Resources/Day1Input')
    fluel = 0
    for line in inp:
        partial = int(line)
        partialFluel = 0
        while True:
            partial = int(partial / 3) - 2
            if (partial > 0):
                partialFluel += partial
            if (partial <= 0):
                break
        fluel += partialFluel
    print fluel

solvePart1()
solvePart2()