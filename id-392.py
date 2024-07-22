'''
392. Is Subsequence
Source: https://leetcode.com/problems/is-subsequence/
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        left, right = 0, 0
        
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1
        
        return left == len(s)
