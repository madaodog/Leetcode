'''
739. Daily Temperatures
Source: https://leetcode.com/problems/daily-temperatures/description/
'''
from typing import List

'''
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, value in enumerate(temperatures):
            while stack and stack[-1][0] < value:
                result[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
            stack.append([value, index])
        return result
    

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
            