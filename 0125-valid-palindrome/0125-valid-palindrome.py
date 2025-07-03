import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #re모듈을 사용해야함
        s=s.lower()
        strs=[]
        for char in s:
            if char.isalnum():
                strs.append(char)
        return strs[::]==strs[::-1]
        