class Solution:
    def isPalindrome(self, x: int) -> bool:
        sign=False
        if x<0:
            return False
        return str(x)==str(x)[::-1]
