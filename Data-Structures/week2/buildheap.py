# uses python3
'''
Task: Create heap from an array of distinct integers
'''
import sys

# declare swaps and number of swaps
NSWAPS = 0
SWAPS = []


def parent(i):
    '''return parent index of input index'''
    return (i - 1) // 2


def leftchild(i):
    '''return left child index of input index'''
    return (2 * i) + 1


def rightchild(i):
    '''return right child index of input index'''
    return (2 * i) + 2


def siftdown(i, size, heap, swaps):
    '''
    shift current node to bottom of heap
    '''

    # minimum priority index
    min_index = i
    # get left child index
    left = leftchild(i)
    # if current node has left child and has less priority than left
    if (left <= size - 1) and (heap[left] < heap[min_index]):
        min_index = left
    # get right child index
    right = rightchild(i)
    # if current node has right child and right has less priority
    # than current min
    if (right <= size - 1) and (heap[right] < heap[min_index]):
        min_index = right
    # if current node has less priority than its child, swap the two
    if i != min_index:
        swaps.append((i, min_index))
        heap[i], heap[min_index] = heap[min_index], heap[i]
        # sift the current node lower
        siftdown(min_index, size, heap, swaps)


def buildheap(size, array, swaps):
    '''
    Build min heap from list of integers.

    Input: number of integers, list of integers, list of swaps made
    Return: first line -> total number of swaps m where 0 <= m <= 4number
            next m lines -> swap operations carried out
    '''
    swaps = []
    # start rectifying heap from second last level
    for i in range((size // 2) - 1, -1, -1):
        siftdown(i, size, array, swaps)
    return swaps

if __name__ == '__main__':
    INPUT = sys.stdin.read().split()
    INPUT = [int(num) for num in INPUT]
    N = INPUT[0]
    NUMBERS = INPUT[1:]

    # build heap
    SWAPS = buildheap(N, NUMBERS, [])
    print(len(SWAPS))
    for item in SWAPS:
        print(item[0], item[1])
