def square_num(n):
    """ Return the square of a number """
    return n ** 2

def compare_list_function(l1, l2):
    """
    Compare two list if element of seconds list are square of element of first list.
    
    """
    l1 = list(map(square_num, l1))

    if list(set(l2) - set(l1)) == []:
        return True

    return False


    
