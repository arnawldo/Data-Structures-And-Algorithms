# uses python3
'''
 The goal of this problem is to represent a given positive integer n as a sum of as many pairwise
distinct positive integers as possible. That is, to find the maximum k such that n can be written as
a 1 + a 2 + · · · + a k where a 1 , . . . , a k are positive integers and a i ̸ = a j for all 1 ≤ i < j ≤ k.'''

import sys

def optimal_summands(n):
    total = n
    summands = []
    i = 1
    while total > 0:
        
        if total == 0:
            break
        if total > 2 * i:
            summands.append(i)
            total -= i
            i += 1
            continue
        else:
            summands.append(total)
            break

    return summands

if __name__ == '__main__':
    SUM = int(sys.stdin.read())
    PTS = optimal_summands(SUM)
    print(len(PTS))
    for p in PTS:
        print(p, end = ' ')
