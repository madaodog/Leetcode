'''
1456. Maximum Number of Vowels in a Substring of Given Length
Source: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        hashset = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        left = 0
        current_vowels = 0
        for i in range(k):
            if s[i] in hashset:
                current_vowels += 1
        max_vowels = current_vowels
        for right in range(k, len(s)):
            if s[left] in hashset and not s[right] in hashset:
                current_vowels -= 1
            elif s[left] not in hashset and s[right] in hashset:
                current_vowels += 1
            max_vowels = max(current_vowels, max_vowels)
            left += 1
        return max_vowels
                
                



        