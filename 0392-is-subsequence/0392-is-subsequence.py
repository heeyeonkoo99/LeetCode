class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if s==t:
            return True
        for i in range(len(t)):
            if not s:
                return True
            if s[j]==t[i] and j<len(s):
                j+=1

            if j==len(s):
                return True
            
            
        return False
            

        