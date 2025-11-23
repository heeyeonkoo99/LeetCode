class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(t)
        k=0
        temp=""
        for i in range(n):
            if k<len(s) and t[i] == s[k] :
                print(t[i],s[k])
                k+=1 
                temp+=t[i]
        
        return temp==s
        
        