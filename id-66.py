'''
66. Plus One
Source: https://leetcode.com/problems/plus-one/description/
'''
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if(digits[i] == 9):
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits



s = Solution()
print(s.plusOne([9]))