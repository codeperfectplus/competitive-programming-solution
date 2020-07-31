'''
Title     : Transpose and Flatten
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 7 May 2020
'''
import numpy

N, M = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(N)], int)
print (array.transpose())
print (array.flatten())
