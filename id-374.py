'''
374. Guess Number Higher or Lower
Source: https://leetcode.com/problems/guess-number-higher-or-lower/
'''
def guess(_):
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (right+left) // 2
            res = guess(mid)
            if res == 0:
                break
            elif res == 1:
                left = mid+1
            elif res == -1:
                right = mid-1
        return mid