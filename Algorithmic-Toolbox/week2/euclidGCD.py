#python3
# Euclidean algorithm for finding greatest common denominator

def euclidGCD(a,b):
    if b==0:
        return a
    a1 = a%b
    return euclidGCD(b,a1)

num1, num2 = map(int, input().split())

print(euclidGCD(num1,num2))
