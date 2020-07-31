'''
Title     : Set .intersection() Operation
Subdomain : Sets
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b,c,d = input(), input().split(),input(), input().split()
print(len(set(b).intersection(set(d))))