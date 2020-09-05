def performOperations(N, op):
    # Write your code here
    # print(N, op)
    a = [i for i in range(1, N + 1)]
    s = sum(a)
    ans = []
    for i in op:
        if i in a:
            a[0], a[-1] = a[-1], a[0]
        else:
            s -= a[-1]
            s += i
            a.pop()
            a.append(i)
        ans.append(s)
    return ans

print(performOperations(3, [4, 2]))
