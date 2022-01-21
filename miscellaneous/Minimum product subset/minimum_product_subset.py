# minimum product subset

import math

def min_product(arr):
    n = len(arr)

    neg_num = 0
    num_zero = 0
    
    for i in range(n):
        if arr[i] == 0:
            num_zero += 1
            continue
        if arr[i] < 0:
            neg_num += 1

    if arr == []:
        return 0

    if n == 1:
        return arr[0]

    if num_zero > 0:
        return 0
    
    if neg_num == 0:
        result = min(arr)
        return result


    if neg_num % 2 != 0:
        result = math.prod(arr)
        return result

    if neg_num % 2 == 0:
        result = math.prod(arr)/min(arr)
        return result
    
