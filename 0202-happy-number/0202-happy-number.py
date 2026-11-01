class Solution:
    def isHappy(self, n: int) -> bool:
        def next(x):
            s=0
            while x:
                d=x%10
                s+=d*d
                x//=10

            return s
        seen=set()
        while n not in seen and n!=1:
            seen.add(n)
            n=next(n)



        return n==1