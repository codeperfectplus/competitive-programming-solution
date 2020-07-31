'''
Title     : Mod Divmod
Subdomain : Math
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b = [int(input()) for _ in range(2)]
result = divmod(a,b)
print(result[0])
print(result[1])
print(result)