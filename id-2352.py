'''
2352. Equal Row and Column Pairs
Source: https://leetcode.com/problems/equal-row-and-column-pairs/description/
'''
from typing import List
from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap = defaultdict(int)
        count = 0

        for row in grid:
            hashmap[tuple(row)] += 1
        
        for col in zip(*grid):
            if tuple(col) in hashmap:
                count += hashmap[tuple(col)]
        
        return count
