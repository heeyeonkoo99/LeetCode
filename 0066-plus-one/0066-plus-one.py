class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        print(s)
        n=int(s)+1
        res=[]
        for i in str(n):
            res.append(int(i))
        return res