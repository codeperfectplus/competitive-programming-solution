'''
Title     : Eye and Identity
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 9 May 2020
'''
import numpy as np

N, M = map(int, input().split())
np.set_printoptions(sign=' ')
print(np.eye(N,M))