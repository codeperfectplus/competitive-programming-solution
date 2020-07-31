'''
Title     : Check Strict Superset
Subdomain : Sets
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
a = set(map(int, input().split()))
f = 0
for i in range(int(input())):
    b = set(map(int, input().split()))
    if len(b.difference(a)) != 0:
        f = 1
    else:
        if len(b) == len(a):
            f =1

if f == 0:
    print('True')
else:
    print('False')