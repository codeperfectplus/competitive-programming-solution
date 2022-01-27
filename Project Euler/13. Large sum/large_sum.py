
""" 
Topic: Large sum
Problem Statement: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

def solver(num, n):
    """ 
    num: big number

    n : first ten digits of sum
    """
    numbers = num.split("\n")
    numbers = [number.strip() for number in numbers]
    numbers = [int(number) for number in numbers if number != ""]


    sum_of_numbers = sum(numbers)

    sliced_number = str(sum_of_numbers)[:n]
    return int(sliced_number)

