import re


def police_catch_thieves(arr, k):
    """ 
    
    arr: array of police thieves index
    k: max distance police can catch thieves
     """
    n = len(arr)

    i = 0
    l = 0
    r = 0 
    res = 0
    thi = []
    pol = []

    # store indices in list
    while i < n:
        if arr[i] == 'P':
            pol.append(i)
        elif arr[i] == 'T':
            thi.append(i)
        i += 1
    
    # track lowest current indices of thief
    while l < len(thi) and r < len(pol):

        if (abs(thi[l] - pol[r]) <= k):
            res += 1
            l += 1
            r += 1
        
        # increment the minimum index
        elif thi[l] < pol[r]:
            l += 1
        else:
            r += 1
    
    return res

if __name__=='__main__':
    arr1 = ['P', 'T', 'T', 'P', 'T']
    k = 2
    print(("Maximum thieves caught: {}".
         format(police_catch_thieves(arr1, k))))

    arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
    k = 2
    print(("Maximum thieves caught: {}".
          format(police_catch_thieves(arr2, k))))