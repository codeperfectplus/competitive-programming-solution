'''
Title     : Check Subset
Subdomain : Sets
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a,b,c,d = input(), input().split(), input(), input().split()
    print( set(b).issubset(set(d)) )
