'''
643. Maximum Average Subarray I
Source: https://leetcode.com/problems/maximum-average-subarray-i/
'''
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        maximum = current_sum
        
        for j in range(k, len(nums)):
            current_sum = current_sum - nums[left] + nums[j]
            maximum = max(maximum, current_sum)
            left += 1
        return maximum / k