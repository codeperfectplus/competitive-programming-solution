'''
Title     : itertools.combinations()
Subdomain : Itertools
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
from itertools import combinations
a, b = input().split()
a = sorted(a)
b = int(b)
for i in range(1,b+1):
    [print(''.join(i)) for i in combinations(a,i)]