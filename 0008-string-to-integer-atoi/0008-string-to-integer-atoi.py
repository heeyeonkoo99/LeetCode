class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT=2**31-1
        MIN_INT=-2**31
        negative=1
        res=0
        i=0

        while i<len(s) and s[i]==" ":
            i+=1
        if i<len(s) and s[i]=="-":
            negative=-1
            i+=1
        elif i<len(s) and s[i]=="+":
            i+=1
        numbers=set("0123456789")
        while i<len(s) and s[i] in numbers:
            res=res*10+int(s[i])
            i+=1
        res=res*negative
        if res<0:
            return max(res, MIN_INT)
        return min(res, MAX_INT)
        