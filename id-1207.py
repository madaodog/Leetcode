'''
1207. Unique Number of Occurences
Source: https://leetcode.com/problems/unique-number-of-occurrences/description/
'''

from collections import defaultdict
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = defaultdict(int)

        for num in arr:
            hashmap[num] += 1
        
        hashset = set(hashmap.values())

        return len(hashset) == len(hashmap.values())