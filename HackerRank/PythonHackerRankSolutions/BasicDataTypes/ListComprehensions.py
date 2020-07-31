'''
Title     : List Comprehensions
Subdomain : Basic Data Types
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ])