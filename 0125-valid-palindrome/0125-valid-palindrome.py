class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res=""
        for i in s:
            if i.isalnum():
                res+=i.lower() 
        if res==res[::-1]:
            return True
        return False