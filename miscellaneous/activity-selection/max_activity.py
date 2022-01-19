from collections import defaultdict


def getMaxActivities(start, finish):
    """
    
    start: list of activity start time
    finish: list of activity finish time
    """
    returnIndex = []
    i = 0
    n = len(start)

    returnIndex.append(i)

    for j in range(n):
        if start[j] >= finish[i]:
            returnIndex.append(j)
            i = j

    return returnIndex