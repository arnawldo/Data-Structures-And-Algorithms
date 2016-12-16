# uses python3

def knapsackWithReps(W, weights, values)
value = {}

for knapsackWeight in range(1, len(W) + 1):
    value[knapsackWeight] = 0
    for itemWeight, itemValue in zip(weights, values):
        if itemWeight <= knapsackWeight:
            val = value[knapsackWeight - itemWeight] + itemValue
            if val > value[knapsackWeight]:
                value[knapsackWeight] = val
return value[W]
