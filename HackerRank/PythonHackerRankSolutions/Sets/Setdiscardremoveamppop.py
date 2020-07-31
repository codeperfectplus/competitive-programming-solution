'''
Title     : Set .discard(), .remove() &amp; .pop()
Subdomain : Sets
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
n = int(input())
s = set(map(int, input().split()))

methods = {
    'pop' : s.pop,
    'remove' : s.remove,
    'discard' : s.discard
}

for _ in range(int(input())):
    method, *args = input().split()

    if len(args) > 1:
        [methods[method](*map(int, arg)) for arg in args]
    else:
        methods[method](*map(int, args))
    
print(sum(s))
