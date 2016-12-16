# uses python3

'''
The goal in this problem is to count the number of inversions of a given sequence.'''

import sys

def merge(b, c):
    # b and c are sorted
    # create empty array for merged b and c
    d = []

    while (len(b) != 0) and (len(c) != 0):
        b1 = b[0]
        c1 = c[0]
        if b1 <= c1:
            d.append(b1)
            del b[0]
        else:
            d.append(c1)
            del c[0]
    if len(b) != 0:
        for i in b:
            d.append(i)
    if len(c) != 0:
        for i in c:
            d.append(i)
    return d


def mergesort(a):
    # if only one element, return it
    if len(a) == 1:
        return a
    # get mid point
    m = len(a) // 2
    # divide array
    b = mergesort(a[0:m])
    c = mergesort(a[m:])
    # merge arrays
    a_merged = merge(b, c)
    return a_merged

MY_ARRAY = [2,3,5,2,4,2,2,9,6,8,5,3,65,6,6,56,4,3]
print(mergesort(MY_ARRAY))
