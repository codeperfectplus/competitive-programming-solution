from math import sqrt
sum = 0
n = 2_000_000
for x in range(1, n+1):
    if x == 1:
        pass
    else:
        half = int(sqrt(x)) + 1
        for y in range(2, half):
            if x % y == 0:
                break
        else:
            sum += x

print(sum)