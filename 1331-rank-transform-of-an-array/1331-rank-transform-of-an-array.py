class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        a=sorted(arr)
        k=1
        dirs={}
        for i in a:
            if i in dirs:
                continue
            dirs[i]=k
            k+=1
        print(dirs)
        res=[]
        for i in arr:
            res.append(dirs[i])
        return res