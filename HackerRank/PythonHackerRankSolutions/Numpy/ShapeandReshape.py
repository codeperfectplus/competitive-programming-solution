'''
Title     : Shape and Reshape
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 06 May 2020
'''
import numpy as np

arr = list(map(int,input().split()))
arr = np.array(arr)

print(np.reshape(arr,(3,3)))

