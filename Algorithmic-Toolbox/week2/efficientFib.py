#python3
# script to calculate the nth fibonacci number

# list of fibonacci numbers


def fibList(n):
    F = [0,1]
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])
    return F[n]

number = int(input())

print(fibList(number))
