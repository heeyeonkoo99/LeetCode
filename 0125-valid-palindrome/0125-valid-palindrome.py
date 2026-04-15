class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        n=len(s)
        for i in s:
            if i.isalnum():
                res+=i.lower() 
        print(res)

        return res==res[::-1]
        