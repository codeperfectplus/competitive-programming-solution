'''
Title     : Power - Mod Power
Subdomain : Math
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b,m = [int(input()) for _ in range(3)]
print(pow(a,b),pow(a,b,m),sep='\n')