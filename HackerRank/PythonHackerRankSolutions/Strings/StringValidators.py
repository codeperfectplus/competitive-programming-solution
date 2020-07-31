'''
Title     : String Validators
Subdomain : Strings
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
if __name__ == '__main__':
    s = input()
    result = ["False", "False", "False", "False", "False"]
    for i in s:
        if i.isalnum():
            result[0] = "True"
        if i.isalpha():
            result[1] = "True"
        if i.isdigit():
            result[2] = "True"
        if i.islower():
            result[3] = "True"
        if i.isupper():
            result[4] = "True"
    print(*result, sep="\n")
