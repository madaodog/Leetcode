'''
1004. Max Consecutive Ones III
Source: https://leetcode.com/problems/max-consecutive-ones-iii/description/
'''

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        changes = k
        max_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                changes -= 1
            while changes < 0:
                if nums[left] == 0:
                    changes += 1
                left += 1
            max_count = max(max_count, right-left+1)
        return max_count
            
