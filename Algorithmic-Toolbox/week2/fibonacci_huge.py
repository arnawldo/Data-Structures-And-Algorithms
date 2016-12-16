# uses python3
#calculate modulus of nth fibonacci number

def fibList(n):
    # function to calculate nth fib number
    F = [0,1]
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])

    return F[n]

def pisano(number):
    # function to calculate pisano period of number
    period = 0
    # create string of moduli
    modulo_string = ''
    # divide through all posible fibonacci numbers
    # until a repetition is detected
    fib_num = 0

    while True:
        mod = fibList(fib_num) % number
        modulo_string += str(mod)
        if len(modulo_string) % 2 == 0:
            if modulo_string[0:len(modulo_string)//2] == modulo_string[len(modulo_string)//2:]:
                period = len(modulo_string) // 2
                break
        fib_num += 1
    return period

print(pisano(3))
