class Solution:
    def addBinary(self, a: str, b: str) -> str:
        temp1=int(a,2)
        temp2=int(b,2)
        #temp1=format(a,"b")
        return format(temp1+temp2,"b")