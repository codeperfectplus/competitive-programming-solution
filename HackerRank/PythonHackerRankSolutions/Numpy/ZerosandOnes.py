'''
Title     : Zeros and Ones
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
import numpy
nums = tuple(map(int, input().split()))
print(numpy.zeros(nums, int))
print(numpy.ones(nums, int))
