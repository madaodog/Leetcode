'''
202. Happy Number
Source: https://leetcode.com/problems/happy-number/description/
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        new_number = n
        numbers = set()
        numbers.add(new_number)
        while(new_number != 1):
            new_number = self.sum_of_squares(new_number)
            if new_number in numbers:
                return False
            numbers.add(new_number)
        return True
    
    def sum_of_squares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output


