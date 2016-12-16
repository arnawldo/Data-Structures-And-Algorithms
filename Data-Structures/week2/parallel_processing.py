# uses python3
'''
Task: Simulate a program that processes a list of jobs in parallel using
      minimum priority queue.
'''
import sys

def parent(i):
    '''return parent index of input index'''
    return (i - 1) // 2


def leftchild(i):
    '''return left child index of input index'''
    return (2 * i) + 1


def rightchild(i):
    '''return right child index of input index'''
    return (2 * i) + 2

def siftdown(i, size, heap):
    '''
    shift current node to bottom of heap
    '''
    # minimum priority index
    min_index = i
    # get left child index
    left = leftchild(i)
    # if current node has left child and has less priority than left
    #NB: priority is multiindex of task load and threadID
    if (left <= size - 1) and (heap[left][0] < heap[min_index][0]):
        min_index = left
    elif (left <= size - 1) and (heap[left][0] == heap[min_index][0]) and \
    (heap[left][1] < heap[min_index][1]):
        min_index = left
    # get right child index
    right = rightchild(i)
    # if current node has right child and right has less priority
    # than current min
    if (right <= size - 1) and (heap[right][0] < heap[min_index][0]):
        min_index = right
    elif (right <= size - 1) and (heap[right][0] == heap[min_index][0]) and \
    (heap[right][1] < heap[min_index][1]):
        min_index = right

    # if current node has less priority than its child, swap the two
    if i != min_index:
        heap[i], heap[min_index] = heap[min_index], heap[i]
        # sift the current node lower
        siftdown(min_index, size, heap)


if __name__ == '__main__':
    INPUT = sys.stdin.read().split()
    INPUT = [int(item) for item in INPUT]
    # nested lists of [priority, threadID]
    # [[0, 0], [0, 1], [0, 2], .....]
    THREADS = [[0, threadID] for threadID in range(0, INPUT[0])]
    TASKS = INPUT[2:]
    # for task in TASKS
    for task in TASKS:
        # increase priority of current min priority THREAD
        print(THREADS[0][1], THREADS[0][0]) # print current thread & time start
        THREADS[0][0] += task
        # sift this task down the priority queue
        siftdown(0, INPUT[0], THREADS)
