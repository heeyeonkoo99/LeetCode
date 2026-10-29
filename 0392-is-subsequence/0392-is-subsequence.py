class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        
        if s=="":
            return True
        for j in range(len(t)):
            if t[j]==s[i]:
                print(j, s[i])
                i+=1
            if i==len(s):
                return True
        print(i)
        return  False