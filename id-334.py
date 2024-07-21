'''
334. Increasing Triplet Subsequence
Source: https://leetcode.com/problems/increasing-triplet-subsequence/
''' 
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        # Initialize `left` and `mid` to positive infinity
        left = float('inf')
        mid = float('inf')
        
        for num in nums:
            if num <= left:
                left = num
            elif num <= mid:
                mid = num
            else:  # Here num > mid, so we found a valid triplet
                return True
        
        return False
