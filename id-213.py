'''
213. House Robber II
Source: https://leetcode.com/problems/house-robber-ii/
'''
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
    
    def rob_helper(self, nums: List[int]) -> int:
        ptr1, ptr2 = 0
        for num in nums:
            temp = max(num+ptr1, ptr2)
            ptr1 = ptr2
            ptr2 = temp
        return ptr2
