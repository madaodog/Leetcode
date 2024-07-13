'''
283. Move Zeroes
Source: https://leetcode.com/problems/move-zeroes/description/
'''
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 0
        while right < len(nums):
        # if nums[left] == 0 & nums[right] == 0, increment nums[right] until != 0
            if nums[left] == 0 and nums[right] == 0:
                right += 1
        # if nums[left] == 0 & nums[right] != 0, swap nums[left] with nums[right]
            elif nums[left] == 0 and nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                right += 1
                left += 1
        # otherwise increment left and right
            else:
                right += 1
                left += 1
        return nums
    

s = Solution()
print(s.moveZeroes([1,0,3,0,0,5,0]))

