from globalFunctions import readInputFile

def solvePart1(options = (12, 2)):
    inp = readInputFile('../Resources/Day2Input')
    program = inp[0].split(',')
    program[1] = options[0]
    program[2] = options[1]
    return readOpcode(program)

def solvePart2():
    inp = readInputFile('../Resources/Day2Input')
    for i in range(0, 100):
        for j in range(0, 100):
            result = solvePart1([i, j])
            if result == 19690720:
                return 100 * i + j

def readOpcode(program):
    idx = 0
    while program[idx] != '99':
        type = 'sum' if (program[idx] == '1') else 'prod'
        firstOperator = int(program[idx+1])
        secondOperator = int(program[idx+2])
        resultIdx = int(program[idx+3])
        program[resultIdx] = int(program[firstOperator]) + int(program[secondOperator]) if type == 'sum' else int(program[firstOperator]) * int(program[secondOperator])
        idx += 4
    return program[0]

print solvePart1()
print solvePart2()