'''
Title     : Dot and Cross
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 9 May 2020
'''

import numpy as np
N = int(input())
A = np.array([input().split() for _ in range(N)],int)
B = np.array([input().split() for _ in range(N)],int)

print(A@B)
