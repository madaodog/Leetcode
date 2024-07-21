'''
345. Reverse Vowels of a String
Source: https://leetcode.com/problems/reverse-vowels-of-a-string/
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack = []
        reversed = ''
        for letter in s:
            if letter in vowels:
                stack.append(letter)
        for index, letter in enumerate(s):
            if letter in vowels:
                reversed += stack.pop()
            else:
                reversed += letter
        return reversed




        