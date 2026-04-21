class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if not s:
            return True
        for i in range(len(t)):
            if t[i]==s[j] and j<len(s):
                print(i,j)
                j+=1
            if j==len(s):
                return True
        return False