'''
Title     : Integers Come In All Sizes
Subdomain : Math
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b, c, d = [int(input()) for _ in range(4)]
result = pow(a,b) + pow(c,d)
print(result)
