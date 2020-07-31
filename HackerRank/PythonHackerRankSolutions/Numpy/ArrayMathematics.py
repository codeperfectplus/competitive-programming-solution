'''
Title     : Array Mathematics
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
import numpy as np
N, M = map(int, input().split() )
a = np.array([input().split()], int) 
b = np.array([input().split()], int)
print(a + b)
print(a - b)
print(a * b)
print(a//b)
print(a%b)
print(a**b)