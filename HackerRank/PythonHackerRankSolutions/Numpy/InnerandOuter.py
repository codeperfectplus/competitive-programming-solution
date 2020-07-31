'''
Title     : Inner and Outer
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 9 May 2020
'''
import numpy as np
a = np.array(input().split(),int)
b = np.array(input().split(),int)

print(np.inner(a,b))
print(np.outer(a,b))