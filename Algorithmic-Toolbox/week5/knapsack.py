# uses python3

'''
    Problem Introduction
This problem is about implementing an algorithm for the knapsack without
repetitions problem.
    Problem Description
Task.
In this problem, you are given a set of bars of gold and your goal is to take
as much gold as possible
into your bag. There is just one copy of each bar and for each bar you can
either take it or not (hence
you cannot take a fraction of a bar).
Input Format.
The first line of the input contains the capacity W of a knapsack and
the number n of bars of gold.
The next line contains n integers w 0 , w 1 , . . . , w n−1
defining the weights of the bars of gold.
Constraints.
1 ≤ W ≤ 10^4 ; 1 ≤ n ≤ 300; 0 ≤ w_0 , . . . , w_n−1 ≤ 10^5 .
Output Format.
Output the maximum weight of gold that fits into a knapsack of capacity W .'''

import sys

def knapsack(totalWeight, bars):
    # create optimal weights table initialized to zero
    weightTable = [[0] * (len(bars) + 1) for i in range(totalWeight + 1)]

    for gold_bar in range(1, len(bars) + 1):
        for sackWeight in range(1, totalWeight + 1):
            weightTable[sackWeight][gold_bar] = weightTable[sackWeight][gold_bar - 1]
            if bars[gold_bar - 1] <= sackWeight:
                currentWeight = weightTable[sackWeight - bars[gold_bar - 1]][gold_bar - 1] + bars[gold_bar - 1]
                if weightTable[sackWeight][gold_bar] < currentWeight:
                    weightTable[sackWeight][gold_bar] = currentWeight
    return weightTable[totalWeight][len(bars)]

if __name__ == '__main__':
    INPUT = [int(n) for n in sys.stdin.read().split()]
    WEIGHT = INPUT[0]
    BARS = INPUT[2:]
    print(knapsack(WEIGHT, BARS))
