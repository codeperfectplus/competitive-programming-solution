""" 
Problem Statement: Power Digit Sum

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def solver(num, power):
    sum = 0
    multiply = pow(num, power)

    for i in str(multiply):
        sum += int(i)
    return sum
