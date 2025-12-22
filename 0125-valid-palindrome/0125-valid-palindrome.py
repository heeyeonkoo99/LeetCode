class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        res=""
        for i in s:
            if i.isalnum():
                res+=i.lower()
        return res==res[::-1]
        