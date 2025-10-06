class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        
        for i in s:
            if i=="#" :
                if s1:
                    s1.pop(-1)
            else:
                s1.append(i)
        for i in t:
            if i=="#":
                if s2:
                    s2.pop(-1)
            else:
                s2.append(i)

        return "".join(s1)=="".join(s2)
        
        