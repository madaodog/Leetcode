'''
605. Can Place Flowers
Source: https://leetcode.com/problems/can-place-flowers/description
'''

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible_flowers = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    possible_flowers += 1
                    if possible_flowers >= n:
                        return True
        
        return possible_flowers >= n
