# uses python3

import sys

'''
The goal in this problem is to find the last digit of a sum of the first n Fibonacci numbers.
'''


def sum_last_digit(number1, number2):
    # pisano period of mod 10 is 60
    # find mod of given number
    mod10_index = (number2 % 60) + 2
    # find mod of F(n+2)
    F = [0,1]
    for i in range(2, mod10_index+1):
        F.append(F[i-1]+F[i-2])
    total1 = F[mod10_index] - 1
    mod10_index = ((number1 - 1) % 60) + 2
    F = [0,1]
    for i in range(2, mod10_index+1):
        F.append(F[i-1]+F[i-2])
    total2 = F[mod10_index] - 1
    return (total1 - total2) % 10

if __name__ == '__main__':
    input_numbers = [int(element) for element in sys.stdin.read().split()]
    M = input_numbers[0]
    N = input_numbers[1]
    print(sum_last_digit(M, N))
