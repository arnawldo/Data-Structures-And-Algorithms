# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)


def maxPairwiseProduct(n, numbers):
    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if numbers[i]*numbers[j] > result:
                result = numbers[i]*numbers[j]

    return result

def maxPairwiseProductFast(n, numbers):

    max_index1 = -1
    for i in range(0, n):
        if (max_index1 == -1) or (numbers[i]>numbers[max_index1]):
            max_index1 = i

    max_index2 = -1
    for j in range(0, n):
        if (numbers[j] is not numbers[max_index1]) and ((max_index2 == -1) or (numbers[j]>numbers[max_index2])):
            max_index2 = j
    #print(max_index1,max_index2)
    return numbers[max_index1] * numbers[max_index2]


print(maxPairwiseProductFast(n,a))
