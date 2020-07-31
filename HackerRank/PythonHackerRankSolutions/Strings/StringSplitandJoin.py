'''
Title     : String Split and Join
Subdomain : Strings
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = '-'.join(line)
    return line

if __name__ == '__main__':