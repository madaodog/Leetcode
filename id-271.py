'''
271. Encode and Decode Strings
Source: https://leetcode.com/problems/encode-and-decode-strings
'''
from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            strs.append(s[j+1:j+1+length])
            i = j+1+length
        return strs





s = Solution()
print(s.encode(["neet","code","love","you"]))
print(s.decode(s.encode(["neet","code","love","you"])))
