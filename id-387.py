'''
387. First Unique Character in a String
Source: https://leetcode.com/problems/first-unique-character-in-a-string/description/
'''
import heapq

class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for i in range(len(s)):
            # if not present, create new entry
            if s[i] not in map:
                map[s[i]] = 1
            # if present, increment entry
            else:
                map[s[i]] += 1
        for index, key in enumerate(s):
            if map[key] == 1:
                return index
        return -1
        
