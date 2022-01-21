import math

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

    if pos_num == 0:
        result = 0

    if neg_num % 2 == 0:
        result = math.prod(arr)
        return result

    if neg_num % 2 != 0:
        result = math.prod(arr)/min(arr)
        return int(result)
