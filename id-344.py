'''
344. Reverse String
Source: https://leetcode.com/problems/reverse-string/description/
'''
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

s = Solution()
print(s.reverseString(["h","e","l","l","o"]))