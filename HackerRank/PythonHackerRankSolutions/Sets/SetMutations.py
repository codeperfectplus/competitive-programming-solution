'''
Title     : Set Mutations
Subdomain : Sets
Domain    : Python
Author    : codeperfectplus
Created   : 6 May 2020
'''

_, L = input(), set(input().split())
for _ in range(int(input())):
    getattr(L, input().split()[0])(set(input().split()))
print(sum(map(int, L)))