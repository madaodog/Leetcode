'''
22. Generate Parentheses
Source: https://leetcode.com/problems/generate-parentheses/description/
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # there have to be n opening and n closing brackets
        # at any point there can't be more closing brackets than opening brackets
        opening, closing = 0, 0
        stack = []
        result = []
        
        def backtrack(opening, closing):
            if opening == closing == n:
                result.append("".join(stack))
                return
            
            if opening < n:
                stack.append("(")
                backtrack(opening+1, closing)
                stack.pop()
            
            if closing < opening:
                stack.append(")")
                backtrack(opening, closing+1)
                stack.pop()
                
        backtrack(opening, closing)
        return result