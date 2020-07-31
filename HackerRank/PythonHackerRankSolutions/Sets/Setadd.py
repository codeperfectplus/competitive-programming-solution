'''
Title     : Set .add()
Subdomain : Sets
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Method List Conprehension
value  = [(input()) for x in range(int(input()))]
print(len(set(value)))




# Alternate Option To 
""" N = int(input())  # sTake Input For How Many Country
list = []           #List to store country name
for _ in range(N):  # for loop to take input   
    list.append( input()) # append value in list
print(len(set(list))) """