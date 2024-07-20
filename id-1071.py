'''
1071. Greatest Common Divisor of Strings
Source: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0
        if len(str1) >= len(str2):
            gcd = str2
        else:
            gcd = str1
        while not self.isDivisor(str1, gcd) or not self.isDivisor(str2, gcd) and len(gcd) > 0:
            gcd = gcd[:-1]
        return gcd
    

    def isDivisor(self, str1: str, divisor: str) -> str:
        if len(divisor) > 0:
            multiplication = len(str1) // len(divisor)
            return (multiplication * divisor) == str1
        else:
            return True