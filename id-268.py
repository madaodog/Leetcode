'''
268. Missing Number
Source: https://leetcode.com/problems/missing-number/description/
'''

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([i for i in range(0, len(nums)+1)]) - sum(nums) 
    
