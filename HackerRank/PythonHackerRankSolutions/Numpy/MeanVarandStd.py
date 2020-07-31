'''
Title     : Mean, Var, and Std
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 9 May 2020
'''
import numpy as np

N, M = map(int, input().split())
array = np.array([input().split() for _ in range(N)],int)
np.set_printoptions(legacy='1.13')
print(np.mean(array, axis=1))
print(np.var(array, axis=0))
print(np.std(array, axis=None))
