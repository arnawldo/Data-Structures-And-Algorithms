# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    W = capacity

    #list of lists containing value, weight, value per kg = density
    wvd = [[v, w, float(v/w)] for v, w in zip(values, weights)]
    #sort list according to density
    wvd = sorted(wvd, key=lambda x: x[2], reverse=True)
    #iterate through wvd adding into knapsack
    for i in wvd:
        #if sack is not empty and item doesnt fill sack, add all of it
        if W > 0 and i[1] <= W:
            value += i[0]
            W -= i[1]
        elif W > 0 and i[1] > W:
            value += i[2] * W
            break

    return value


if __name__ == "__main__":
    data = [int(word)for word in sys.stdin.read().split()]
    N, CAPACITY = data[0:2]
    VALUES = data[2:(2 * N + 2):2]
    WEIGHTS = data[3:(2 * N + 2):2]

    opt_value = get_optimal_value(CAPACITY, WEIGHTS, VALUES)
    print("{:.10f}".format(opt_value))
