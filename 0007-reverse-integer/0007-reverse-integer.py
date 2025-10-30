class Solution:
    def reverse(self, x: int) -> int:
        if x is None:
            return
        minus=False
        x=str(x)
        
        if x[0]=="-":
            minus=True
            x=x[1:]
        x=int(x[::-1])

        if minus:
            x=-x
        if x<-2**31 or x>2**31:
            return 0
        return x
        