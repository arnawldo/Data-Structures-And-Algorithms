#python3
# calculate lcm of two numbers
# lcm(a,b) = ab(a,b) / gcd(a,b)

def euclidGCD(a,b):
    if b==0:
        return a
    a1 = a%b
    return euclidGCD(b,a1)

def lcm(a,b):
    return int(a * b // euclidGCD(a,b))

num1, num2 = map(int, input().split())

print(lcm(num1, num2))
