# python3


def change(m):

    counter = 0

    while(True):
        if m > 9:
            m -= 10
            counter += 1
            continue
        if m > 4:
            m -= 5
            counter += 1
            continue
        if m > 0:
            m -= 1
            counter += 1
            continue
        else:
            return counter

number = int(input())
print(change(number))
