'''
1431. Kids With the Greatest Number of Candies
Source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
'''
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies) # O(n)
        booleans = []
        # O(n)
        for candy in candies:
            if candy + extraCandies >= maximum:
                booleans.append(True)
            else:
                booleans.append(False)
        return booleans