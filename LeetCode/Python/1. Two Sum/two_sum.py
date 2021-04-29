""" 
    Topic : Two Sum
    Language : Python
    Problem Statement : Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""
from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, num in enumerate(nums):
            other = target - num 
            
            if other in seen:
                return[seen[other], index]
            else:
                seen[num] = index
        return []

pr = Solution()
res = pr.two_sum([2,7,11,15], 13)
print(res)