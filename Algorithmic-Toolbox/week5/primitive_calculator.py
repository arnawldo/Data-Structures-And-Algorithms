# uses python3

'''You are given a primitive calculator that can perform the
following three operations with the current num-
ber x: multiply x by 2, multiply x by 3, or add 1 to x.
Your goal is given a positive integer n, find the
minimum number of operations needed to obtain the number n
starting from the number 1.

This program will start from the top dividing by 3, 2 and
subtracting 1 to reach one. The same number of
operations will be done as starting form 1 to reach n
'''

import sys

# dictionary of solved number of operations for a number
minOperationsDict = {1: 0}

def primitive_calculator(n):

    for number in range(2, n + 1):

        minOperationsDict[number] = float('inf')

        if number % 3 == 0:
            numOps = 1 + minOperationsDict[number / 3]
            if numOps < minOperationsDict[number]:
                minOperationsDict[number] = numOps
        if number % 2 == 0:
            numOps = 1 + minOperationsDict[number / 2]
            if numOps < minOperationsDict[number]:
                minOperationsDict[number] = numOps
        # number is subtractable by 1
        numOps = 1 + minOperationsDict[number - 1]
        if numOps < minOperationsDict[number]:
            minOperationsDict[number] = numOps


    sequence = [n]
    while n > 1:
        if minOperationsDict[n - 1] == minOperationsDict[n] - 1:
            n -= 1
        elif (n % 2 == 0) and minOperationsDict[n // 2] == minOperationsDict[n] - 1:
            n = n // 2
        elif (n % 3 == 0) and minOperationsDict[n // 3] == minOperationsDict[n] - 1:
            n = n // 3
        sequence.append(n)
    return(sequence)


INPUT = sys.stdin.read()
N = int(INPUT)
# n = 96234
# n = 1
intermediateNums = primitive_calculator(N)
print(len(intermediateNums) - 1)
for x in reversed(intermediateNums):
    print(x, end=' ')
