# Uses python3
'''To force the given implementation of the quick sort algorithm to efficiently process sequences with
few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new
partition procedure should partition the array into three parts: < x part, = x part, and > x part
'''

import sys
import random

def partition3(a, l, r):
    #print('a in', a, 'l', l, 'r', r)
    x = a[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        #print('i', i, 'j', j, 'k', k)
        if a[i] < x and j != k:
            j += 1
            k += 1
            a[i], a[j] = a[j], a[i]
            a[i], a[k] = a[k], a[i]
        elif a[i] < x and j == k:
            j += 1
            k += 1
            a[i], a[j] = a[j], a[i]
        elif a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]
    a[l], a[j] = a[j], a[l]
    #print('a out', a, 'l', l, 'r', r)
    return j, k


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    #print(a, l, r)
    if l >= r:
        #print('returning none')
        return None
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
