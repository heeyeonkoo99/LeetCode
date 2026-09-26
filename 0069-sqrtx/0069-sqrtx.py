class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l,r=1,x
        while l<=r:
            mid=(l+r)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                l+=1
            else:
                r-=1
        return r

        