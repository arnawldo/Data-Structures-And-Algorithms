# uses python3
#calculate modulus of nth fibonacci number

import sys

def huge_fib_mod(fib_ind, modulo_number):
    # list of modulus of Fib numbers
    fm = [0, 1, 1]
    # create sequence of moduli
    # a[i] mod n = (a[i -1] mod n + a[i -1] mod n) mod n
    i = 3
    while True:
        fm.append(((fm[i-1] % modulo_number) + (fm[i-2] % modulo_number)) % modulo_number)
        #print(fm)
        if fm[-2:] == [0, 1]:
            period = len(fm) - 2
            break
        i += 1
    index_mod = fib_ind % period
    return fm[index_mod]

if __name__ == '__main__':
    DATA = [int(element) for element in sys.stdin.read().split()]
    #DATA = 281621358815590, 30524
    N, M = DATA
    print(huge_fib_mod(N, M))
