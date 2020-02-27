from globalFunctions import readInputFile
import sys

def solvePart1():
    inp = readInputFile('../Resources/Day4Input')
    start_number = inp[0].split('-')[0]
    stop_number = inp[0].split('-')[1]
    counter_right_passwords = 0
    for number in range(int(start_number), int(stop_number)):
        double = False
        never_decrease = True
        last_number = 0
        for current_number in str(number):
            if last_number > current_number:
                never_decrease = False
            if last_number == current_number:
                double = True
            last_number = current_number
        if double and never_decrease:
            counter_right_passwords += 1
    return counter_right_passwords

def solvePart2():
    inp = readInputFile('../Resources/Day4Input')
    start_number = inp[0].split('-')[0]
    stop_number = inp[0].split('-')[1]
    counter_right_passwords = 0
    for number in range(int(start_number), int(stop_number)):
    # for number in [718077]:
        doubles = []
        never_decrease = True
        last_number = 0
        double_number = 1
        for current_number in str(number):
            if last_number > current_number:
                never_decrease = False
            if last_number == current_number:
                double_number += 1
            if last_number != current_number:
                doubles.append(double_number)
                double_number = 1
            # print current_number, last_number, double_number
            last_number = current_number
        if double_number > 1:
            doubles.append(double_number)
        # print number, doubles
        if 2 in doubles and never_decrease:
            counter_right_passwords += 1
    return counter_right_passwords

print solvePart1()
print solvePart2()