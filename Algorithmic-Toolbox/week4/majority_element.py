#  Uses python3
'''
The goal in this code problem is to check whether an input sequence contains a majority element.'''

import sys

def get_majority_element(a, left, right):
    if left == right:
        return a[left]
    if right - left == 1:
        if a[right] == a[left]:
            return a[left]
        else:
            return -1
    #write your code here
    mid = (right + left) // 2
    
    left_majority = get_majority_element(a, left, mid)
    right_majority = get_majority_element(a, mid + 1, right)

    if (left_majority != -1) and (a[left : right + 1].count(left_majority) > ((right + 1 - left) // 2)):
        return left_majority
    elif (right_majority != -1) and (a[left: right + 1].count(right_majority) > ((right + 1 -left) // 2)):
        return right_majority

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)
