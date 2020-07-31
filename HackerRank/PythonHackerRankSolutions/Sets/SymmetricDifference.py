'''
Title     : Symmetric Difference
Subdomain : Sets
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,i,m,j = input(),input().split(),input(),input().split()
[print(i) for i in sorted(set(i)^set(j), key = int)]