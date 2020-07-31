'''
Title     : Zipped!
Subdomain : Built-Ins
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split()) 

sheet = []
for _ in range(x):
    sheet.append(map(float, input().split()) ) 

for i in zip(*sheet): 
    print( sum(i)/len(i) )
