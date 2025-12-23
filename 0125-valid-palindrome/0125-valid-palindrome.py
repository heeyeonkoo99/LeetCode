class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        res=""
        i=0
        while i<len(s):
            if s[i].isalnum():
                res+=s[i].lower()
            i+=1
        print(res)
        return res==res[::-1]