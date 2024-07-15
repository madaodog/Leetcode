'''
33. Search in Rotated Sorted Array
Source: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:  # Corrected the condition here
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Determine which part is sorted
            if nums[left] <= nums[mid]:  # Left part is sorted
                if nums[left] <= target < nums[mid]:  # Target is in the left part
                    right = mid - 1
                else:  # Target is in the right part
                    left = mid + 1
            else:  # Right part is sorted
                if nums[mid] < target <= nums[right]:  # Target is in the right part
                    left = mid + 1
                else:  # Target is in the left part
                    right = mid - 1

        return -1  # Target not found

    

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))


            