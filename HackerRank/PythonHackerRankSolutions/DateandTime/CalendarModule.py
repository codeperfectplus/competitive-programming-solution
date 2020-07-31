'''
Title     : Calendar Module
Subdomain : Date and Time
Domain    : Python
Author    : codeperfectplus
Created   : 17 January 2020
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m, d, y = input().split()
d= int(d)
m = int(m)
y = int(y)
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())                                               

