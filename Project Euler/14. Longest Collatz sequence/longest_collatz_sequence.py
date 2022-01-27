""" 
Title: Longest Collatz sequence
Problem Statement: 

    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

#upper_limit = 1_000_000

 """

from ast import Return


def get_number_of_sequence(num):
    returned_num = [num]
    while num > 1:
        if num % 2 == 0:
            num = num / 2
            returned_num.append(int(num))
        else:
            num = 3 * num + 1
            returned_num.append(int(num))
    return len(returned_num)

def solver(upper_limit):
    fullList = {}
    for i in range(2, upper_limit):
        fullList[i] = get_number_of_sequence(i)

    fullList = sorted(fullList.items(), key=lambda x: x[1], reverse=True)
    return fullList[0][0]
        
#837799

# REVIEW: This is a very slow solution. Need to optimize it.
