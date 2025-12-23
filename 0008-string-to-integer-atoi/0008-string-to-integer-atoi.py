class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign=1
        i=0
        res=0
        if not s:
            return 0
        if s[0]=="-" or s[0]=="+":
            sign=-1 if s[0]=="-" else 1
            i+=1
        while i<len(s) and s[i].isdigit():
            res=(res)*10+int(s[i])
            i+=1
            if sign*res<=-2**31:
                return -2**31
            if sign*res>=2**31-1:
                return 2**31-1
        return sign*res