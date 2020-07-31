'''
Title     : Map and Lambda Function
Subdomain : Python Functionals
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
cube = lambda x: pow(x,3)

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        return 0
    elif n==1:
        return 1
    fib_num = [0, 1]
    for i in range(2, n):
        fib_num.append(fib_num[i-1]+fib_num[i-2])
    return fib_num

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))