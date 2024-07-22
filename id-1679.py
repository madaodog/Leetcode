'''
1679. Max Number of K-Sum Pairs
Source: https://leetcode.com/problems/max-number-of-k-sum-pairs
'''
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sorted_list = sorted(nums)
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if sorted_list[left] + sorted_list[right] == k:
                count += 1
                right -= 1
                left += 1
            elif sorted_list[left] + sorted_list[right] > k:
                right -= 1
            elif sorted_list[left] + sorted_list[right] < k:
                left += 1
        return count



