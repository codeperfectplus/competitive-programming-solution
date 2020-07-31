#!/bin/python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(" ")))
# Write Your Code Here

numberOfSwap = 0
for i in range(n):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwap += 1
            if numberOfSwap == 0:
                break

print(f"Array is sorted in {numberOfSwap} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
