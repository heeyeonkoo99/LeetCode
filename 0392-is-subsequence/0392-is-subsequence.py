class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k=0

        for i in range(len(t)):
            if k<len(s) and t[i]==s[k]:
                k+=1
            
        print(k)
        return k==len(s)
        