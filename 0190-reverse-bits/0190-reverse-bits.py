class Solution:
    def reverseBits(self, n: int) -> int:
       a=format(n,"032b")
       return str(int(a,2))[::-1]