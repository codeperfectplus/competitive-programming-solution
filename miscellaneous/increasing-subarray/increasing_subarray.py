# increasing subarray

def increasing_subarray(arr):
    """ strict increasing subarray """
    if len(arr) < 2:
        return len(arr)
    else:
        max_len = 1
        curr_len = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                curr_len += 1
            else:
                curr_len = 1
            max_len = max(max_len, curr_len)
        return max_len
