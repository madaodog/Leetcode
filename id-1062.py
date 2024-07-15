'''
1062. Longest Repeating Substring
Source: 1062. Longest Repeating Substring
'''

'''
Input: s = "XYYX", k = 2

Output: 4

Input: s = "AAABABB", k = 1

s = "ABBBBB"


'''
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            if right - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result
    
s = Solution()
print(s.characterReplacement('XXYY', 2))


