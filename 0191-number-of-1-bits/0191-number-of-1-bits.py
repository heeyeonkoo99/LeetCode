class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        a=bin(n)
        for i in str(a):
            if i=="1":
                cnt+=1

        return cnt
        