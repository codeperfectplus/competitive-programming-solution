'''
Title     : Find the Second Largest Number
Subdomain : Basic Data Types
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
Problem    :
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_list = []
    for i in arr:
        if i not in new_list:
            new_list.append(i)
    sort_list = sorted(new_list)
    print(sort_list[-2])