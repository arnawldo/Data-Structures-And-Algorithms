#python3
# calculate GCD of two numbers

def naiveGCD(a,b):

    best = 0

    for d in range(1,a+b):
        if a%d==0 and b%d==0:
            best = d

    return best

num1 = int(input())
num2 = int(input())

print('GCD is',naiveGCD(num1,num2))
