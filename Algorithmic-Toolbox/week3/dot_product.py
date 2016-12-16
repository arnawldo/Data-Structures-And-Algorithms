#Uses python3

import sys

def max_dot_product(a, b):
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    dot = []
    for i in range(len(a)):
        dot.append(a[i]*b[i])
    return sum(dot) 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
