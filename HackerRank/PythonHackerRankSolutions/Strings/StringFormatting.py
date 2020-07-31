'''
Title     : String Formatting
Subdomain : Strings
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print( "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
""" def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        octa = oct(i)[2:]
        hexa = hex(i)[2:]
        bina = bin(i)[2:]
        print(f"{i}  {octa}  {hexa}  {bina}") """