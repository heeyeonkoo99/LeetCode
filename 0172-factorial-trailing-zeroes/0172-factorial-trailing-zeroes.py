class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt=0
        while n!=0:
            cnt*=n
            n-=1
        return str("cnt").find("0")