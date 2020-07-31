'''
Title     : Sum and Prod
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 9 May 2020
'''
import numpy
N, M = map(int, input().split())
array1 = numpy.array([input().strip().split() for _ in range(N)], int)
array2 = numpy.sum(array1,axis=0)
print(numpy.prod(array2))