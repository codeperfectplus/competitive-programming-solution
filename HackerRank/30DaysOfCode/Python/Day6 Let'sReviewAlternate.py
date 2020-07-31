# Enter your code here. Read input from STDIN. Print output to STDOUT
# read the input


def solution(string):
    even = ""
    odd = ""
    for j in range(len(string)):
        if j % 2 == 0:
            even = even + string[j]
        else:
            odd = odd + string[j]
    print(even + " " + odd)


N = int(input())
for i in range(0, N):
    string = input()

    solution(string)
