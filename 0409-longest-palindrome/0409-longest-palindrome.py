from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return ""
        length=0
        cnt=Counter(s)
        odd=False

        for i in cnt.values():
            if i%2==0:
                length+=i
            else:
                length+=i-1
                odd=True
        if odd:
            length+=1
        return length

        