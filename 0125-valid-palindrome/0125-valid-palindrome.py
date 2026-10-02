class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]

        for i in s:
            if i.isalnum():
                res.append(i.lower())
        temp="".join(res)
        return temp==temp[::-1]
        