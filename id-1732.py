'''
1732. Find the Highest Altitude
Source: https://leetcode.com/problems/find-the-highest-altitude/description/
'''
from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = 0
        for altitude in gain:
            current += altitude
            highest = max(current, highest)
        return highest
