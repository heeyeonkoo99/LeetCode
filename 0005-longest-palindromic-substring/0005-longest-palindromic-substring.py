class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return l+1,r-1
        start,end=0,0
        for i in range(len(s)-1):
            s1,e1=expand(i,i)
            if e1-s1>end-start:
                start,end=s1,e1
            s2,e2=expand(i,i+1)
            if e2-s2>end-start:
                start,end=s2,e2
        return s[start:end+1]
            