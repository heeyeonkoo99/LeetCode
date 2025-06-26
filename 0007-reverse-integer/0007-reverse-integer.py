class Solution:
    def reverse(self, x: int) -> int:
        # 최대한 간단하게 짤수있는걸 생각해보자!
        sign=-1 if x<0 else 1
        reversed_int=int(str(abs(x))[::-1])*sign
        if reversed_int<-2**31 or reversed_int>2**31-1:
            return 0
        return reversed_int

