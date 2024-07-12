'''
88. Merge Sorted Array
Source: https://leetcode.com/problems/merge-sorted-array/description/
'''
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = m - 1
        right = n - 1
        last_idx = len(nums1) - 1

        while left >= 0 and right >= 0:
            if nums1[left] <= nums2[right]: 
                nums1[last_idx] = nums2[right]
                last_idx -= 1
                right -= 1
            else:
                nums1[last_idx] = nums1[left]
                last_idx -= 1
                left -= 1

        while right >= 0:
            nums1[last_idx] = nums2[right]
            last_idx -= 1
            right -= 1