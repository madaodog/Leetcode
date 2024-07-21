'''
151. Reverse Word in a String
https://leetcode.com/problems/reverse-words-in-a-string/
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        word = ''
        stack = []
        index = 0
        while index < len(s):
            if s[index] != ' ':
                word += s[index]
                index += 1
            else:
                if word:
                    stack.append(word)
                    word = ''
                while index < len(s) and s[index] == ' ':
                    index += 1
        if word:
            stack.append(word)
        return ' '.join(stack[::-1])
                

        