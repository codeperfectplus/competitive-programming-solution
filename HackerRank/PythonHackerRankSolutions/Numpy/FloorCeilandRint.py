'''
Title     : Floor, Ceil and Rint
Subdomain : Numpy
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
import numpy as np
np.set_printoptions(sign=' ')
myArray = np.array(input().split(), float)
print(np.floor(myArray))
print(np.ceil(myArray))
print(np.rint(myArray))