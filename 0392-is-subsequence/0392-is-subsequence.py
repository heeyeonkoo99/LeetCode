class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp=""
        index=0
        for i in t:
            if index<len(s) and s[index]==i:
                temp+=i
                index+=1
        return temp==s
        