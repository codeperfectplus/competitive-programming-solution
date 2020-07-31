'''
Title     : itertools.permutations()
Subdomain : Itertools
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
""" Method 1  """
from itertools import permutations
a, b = input().split()
[print(''.join(i)) for i in permutations(sorted(a), int(b))]


""" Method 2 """

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
a , b = input().split()
a = sorted(a)
b = int(b)

for i in permutations(a,b):
    print(''.join(i))



