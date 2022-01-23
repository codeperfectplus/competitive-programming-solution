import math

from numpy import mat


def max_product(arr):
    n = len(arr)

    num_zero = 0
    pos_num = 0
    neg_num = 0

    for i in range(n):
        if arr[i] == 0:
            num_zero += 1
            continue
        if arr[i] > 0:
            pos_num += 1
        if arr[i] < 0:
            neg_num += 1

    if arr == []:
        return 0

    if n == 1:
        return arr[0]

    if num_zero > 0:
        return 0

    if neg_num == 0:
        return math.prod(arr)
    
    if pos_num == 0:
        if neg_num % 2 == 0:
            return math.prod(arr)
        
        if neg_num % 2 == 1:
            return math.prod(arr) / max(arr)
    
    if neg_num % 2 == 0:
        return math.prod(arr)
    
    if neg_num % 2 == 1:
        negative_nums = []
        for i in range(n):
            if arr[i] < 0:
                negative_nums.append(arr[i])
        return math.prod(arr) / max(negative_nums)
