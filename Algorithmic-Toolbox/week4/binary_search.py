# Uses python3
'''The goal in this code problem is to implement the binary search algorithm.
'''
import sys

def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        # mid point
        mid = (left + right) // 2
        # if key in mid point
        if x == a[mid]:
            return mid
        # else if key less than mid value, continue with bottom half
        elif x < a[mid]:
            right = mid - 1
            continue
        # else key is more than mid value, continue with upper half
        else:
            left = mid + 1
            continue
        # return -1 if not found
    return -1


    # if array empty, return -1
    if left > right:
        return left - 1
    # find mid point
    mid = left + ((right - left) // 2)
    # if key in mid point, return mid
    if x == a[mid]:
        return mid
    # if less than mid value, return search on bottom half of array
    elif x < a[mid]:
        return binary_search(a[left:mid], x)
    #if more than mid value, return search on upper half of array
    else:
        return binary_search(a[mid+1:], x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
