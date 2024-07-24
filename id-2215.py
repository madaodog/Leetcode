'''
2215. Find the Difference of Two Arrays
Source: https://leetcode.com/problems/find-the-difference-of-two-arrays/description
'''
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hashset1 = set(nums1)
        hashset2 = set(nums2)
        result1 = set()
        result2 = set()

        for num in hashset1:
            if num not in hashset2:
                result1.add(num)
        
        for num in hashset2:
            if num not in hashset1:
                result2.add(num)
        
        return [list(result1), list(result2)]
