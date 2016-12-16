#python3
# retrieve last digit of nth fibonacci number

# list of fibonacci numbers
F = [0,1]

def fibList(n):

    for i in range(2,n+1):
        #append last digit of nth fibonacci number
        F.append((F[i-1]+F[i-2]) % 10)
    return F[-1]

number = int(input())

print(fibList(number))
