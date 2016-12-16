#python3
# script to calculate nth fibonacci number

def fibRecurs(n):
    if n<=1:
        return n
    else:
        return fibRecurs(n-1) + fibRecurs(n-2)

number = int(input())

print(fibRecurs(number))
