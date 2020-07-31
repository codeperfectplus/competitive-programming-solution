'''
Title     : Min and Max
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 9 May 2020
'''
import numpy as np

N, M = map(int,input().split())

array1 = np.array([input().split() for _ in range(N)],int)
print(np.max(np.min(array1,axis=1)))
