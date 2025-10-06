class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        a=bin(n)[2:]
        print(a)
        for i in a:
            if i=="1":
                cnt+=1
        return cnt

        