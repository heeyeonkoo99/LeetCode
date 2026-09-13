class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1

        while left<=right:
            if s[left]!=s[right]:
                small=min(s[left],s[right])
                s[left]=small
                s[right]=small
            right-=1
            left+=1
        return "".join(s)

  
        