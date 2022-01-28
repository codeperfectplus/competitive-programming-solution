"""
Title: Parallel Universe

Description: find the minimum cost of relocating all the residents to the desired planet 
            to make the population of all the planets equal.
"""

def minimumCost(length, arr):
    mean = int(sum(arr) / length)
    remains = {}
    cost = 0
    for i in range(length):
        if arr[i] > mean:
            remains[i] = arr[i] - mean
            arr[i] = arr[i] - (arr[i] - mean)

    for i in range(length):
        if arr[i] < mean:
            wanted_num = mean - arr[i]
            for key, value in remains.items():
                if value >= wanted_num:
                    # we will go clock wise from the key
                    if i > key:
                        cost += abs(mean * (i - key))
                        arr[i] = arr[i] + wanted_num
                        remains[key] = remains[key] - wanted_num
                        break
                    else:
                        cost += mean* (length - (key - i))
                        arr[i] = arr[i] + wanted_num
                        remains[key] = remains[key] - wanted_num
                        break

    return cost