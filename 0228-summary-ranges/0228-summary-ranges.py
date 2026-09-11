class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]

        temp=[nums[0]]
        for n in nums[1:]:
            if n -1 in temp:
                temp.append(n)
            else:
                print(temp)
                res.append(str(str(temp[0])+"->"+str(temp[-1])))
                temp=[]

        return res

        