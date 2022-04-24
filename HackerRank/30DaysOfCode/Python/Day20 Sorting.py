#!/bin/python3
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(" ")))
# Write Your Code Here

def solver(arr):
    numberOfSwap = 0
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                numberOfSwap += 1
                if numberOfSwap == 0:
                    break
    
    return numberOfSwap, a[0], a[-1]

numberOfSwap, first, last = solver(a)
print(f"Array is sorted in {numberOfSwap} swaps.")
print(f"First Element: {first}")
print(f"Last Element: {last}")
