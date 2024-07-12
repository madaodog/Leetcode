'''
69. Sqrt(x)
Source: https://leetcode.com/problems/sqrtx/description/
'''
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left, right = 0, x
        while left <= right:
            mid = (left+right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
        return right
        
    
s = Solution()
print(s.mySqrt(5))
