# uses python3

'''
The goal in this problem is to count the number of inversions of a given sequence.'''

import sys

def merge(b, b_inversions, c, c_inversions):
    # b and c are sorted
    # create empty array for merged b and c
    d = []
    inversions = b_inversions + c_inversions

    while (len(b) != 0) and (len(c) != 0):
        b1 = b[0]
        c1 = c[0]


        if b1 <= c1:
            d.append(b1)
            del b[0]
        else:
            inversions += len(b)
            d.append(c1)
            del c[0]
    if len(b) != 0:
        d.extend(b)
    if len(c) != 0:
        d.extend(c)
    return d, inversions


def mergesort(a):
    # if only one element, return it
    if len(a) == 1:
        return a, 0
    # get mid point
    m = len(a) // 2
    # divide array
    b, b_inversions = mergesort(a[0:m])
    c, c_inversions = mergesort(a[m:])
    # merge arrays
    a_merged, a_inversions = merge(b, b_inversions, c, c_inversions)
    return a_merged, a_inversions

if __name__ == '__main__':
    INPUT_ARRAY = [int(n) for n in sys.stdin.read().split()[1:]]
    print(mergesort(INPUT_ARRAY)[1])
