# uses python3
import sys

'''
Implementation of tree structure and methods to find tree height
'''
def create_tree(children, parents):
    '''
    Returns tree structure
    Input: number of children, list of parents
    Output: tree in dict format
    '''
    # initialize tree dictionary
    tree = {}
    # iterate through child and parent nodes
    for child, parent in zip(range(children), parents):
        # if parent exists, add child
        if parent in tree:
            tree[parent].append(child)
        # else, add parent and child
        else:
            tree[parent] = [child]
    return tree

def tree_height(tree):
    '''
    Returns tree height
    Input: tree dictionary
    Output: height of tree
    '''
    # set current nodes [root]
    current = tree[-1]
    # height of tree
    height = 0
    # loop through levels
    while len(current):
        height += 1
        # create list for next children
        nodes = []
        # for node in current level, grab children
        for node in current:
            if node in tree:
                nodes.extend(tree[node])
        current = nodes
    return height

if __name__ == '__main__':
    INP = sys.stdin.read()
    INP = [int(item) for item in INP.split()]
    TREE = create_tree(INP[0], INP[1:])
    print(tree_height(TREE))
