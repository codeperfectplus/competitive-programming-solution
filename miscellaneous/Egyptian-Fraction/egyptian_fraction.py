import math

def egyptianFraction(nr, dr):
    """ 
    nr: numerator
    dr: dominator
    
    """
    results = []

    if nr == 0:
        return results
    
    elif nr > dr:
        return results
    
    while nr != 0:
        x = math.ceil(dr / nr)
        results.append(x)

        nr = nr * x - dr
        dr = dr * x

    return results