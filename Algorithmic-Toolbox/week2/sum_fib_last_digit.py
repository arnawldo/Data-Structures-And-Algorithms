# uses python3

import sys

'''
The goal in this problem is to find the last digit of a sum of the first n Fibonacci numbers.
'''
def sum_last_digit(number):
    # pisano period of mod 10 is 60
    # find mod of given number
    mod10_index = (number % 60) + 2
    # find mod of F(n+2)
    F = [0,1]
    for i in range(2, mod10_index+1):
        F.append(F[i-1]+F[i-2])
    
    return (F[mod10_index] -1 ) % 10
if __name__ == '__main__':
    input_number = int(sys.stdin.read())
    print(sum_last_digit(input_number))
