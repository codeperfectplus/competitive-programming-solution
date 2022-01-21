# Problem Statement 

Given an array a, we have to find the minimum product possible with the subset of elements present in the array. The minimum product can be a single element also.

Input : [ -1, -1, -2, 4, 3 ]
Output : -24
Explanation : Minimum product will be ( -2 * -1 * -1 * 4 * 3 ) = -24

Input : [-1, 0 ]
Output : -1
Explanation : -1(single element) is minimum product possible
 
Input : [0, 0, 0 ]
Output : 0

# Approach:

`Greedy Algorithm`

1. If there are an odd number of negative numbers, the result is the product of all non-zero numbers.
2. If there are an even number of negative numbers, the result is the product of all non-zero numbers except the largest valued negative number.
3. If there are zeros and no negative numbers, the result is zero.
4. If all numbers are positive, the result is the least valued number
