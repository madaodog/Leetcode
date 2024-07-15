'''
153. Find Minimum in Rotated Sorted Array
Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
'''
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1 rotation: [0,1,2,3,4] => [4,0,1,2,3]
        # 2 rotations: [0,1,2,3,4] => [3,4,0,1,2]
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] >= nums[left] and nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid-1
        return nums[left]


s = Solution()
print(s.findMin([3,4,5,1,2]))

            
