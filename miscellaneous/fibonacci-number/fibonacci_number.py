# Fibonacci Sequence

def fibonacci_series(input_num):
    ''' 
    args: input_num
    returns: fibonacci series
    '''
    
    prev_num = 0
    curr_num = 1

    if input_num == 0:
        return 0
    
    elif input_num == 1:
        return prev_num
    
    elif input_num == 2:
        return curr_num    
    
    output_list = [prev_num, curr_num]
    # we already have the first two numbers in the list
    # so we start from the third number
    for _ in range(2, input_num):
        new_num = prev_num + curr_num
        prev_num = curr_num
        curr_num = new_num
        output_list.append(new_num)
    return new_num
