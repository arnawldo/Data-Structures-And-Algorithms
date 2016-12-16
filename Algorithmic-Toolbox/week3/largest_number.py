# uses python3
'''
Compose the largest number out of a set of integers.'''
import sys

def isGreaterOrEqual(a, b):

    j = a + b
    k = b + a
    if j >= k:
        return True
    else:
        return False


def largest_number(digits):
    answer = ''
    while len(digits) > 0:
        maxDigit = '-1'
        for digit in digits:
            if isGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
        answer += maxDigit
        del digits[digits.index(maxDigit)]
    return answer

if __name__ == '__main__':
    NUMS = [i for i in sys.stdin.read().split()[1:]]

    print(largest_number(NUMS))
