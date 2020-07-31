'''
Title     : Tuples
Subdomain : Basic Data Types
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

print(hash(tuple(integer_list)))
