'''
567. Permutation in String
Source: https://leetcode.com/problems/permutation-in-string/description/
'''



'''
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        counts_s1 = [0] * 26
        counts_s2 = [0] * 26

        for i in range(n1):
            counts_s1[self.letter_to_number(s1[i])] += 1
            counts_s2[self.letter_to_number(s2[i])] += 1
        
        if counts_s1 == counts_s2:
            return True

        left = 0
        for right in range(len(s1),len(s2)):
            counts_s2[self.letter_to_number(s2[right])] += 1
            counts_s2[self.letter_to_number(s2[left])] -= 1
            if counts_s1 == counts_s2:
                return True
            left += 1
        return False
        
    def letter_to_number(self, letter):
        return ord(letter) - ord('a') 


s = Solution()
print(s.checkInclusion("rokx", "otrxvfszxroxrzdsltg"))


    


