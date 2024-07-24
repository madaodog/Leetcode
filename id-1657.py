'''
1657. Determine if Two Strings Are Close
Source: https://leetcode.com/problems/determine-if-two-strings-are-close/description/
'''

from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        
        for letter in word1:
            freq1[letter] += 1
        
        for letter in word2:
            freq2[letter] += 1
        
        if set(freq1.keys()) != set(freq2.keys()):
            return False
        
        count_freq1 = defaultdict(int)
        count_freq2 = defaultdict(int)
        
        for count in freq1.values():
            count_freq1[count] += 1
        
        for count in freq2.values():
            count_freq2[count] += 1
        
        return count_freq1 == count_freq2
