class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()를 하지않고 원래 인덱스에서 바꾸는게 필요함!
        res=[]
        if len(nums)==0:
            return []
        for i in range(len(nums)):
            temp=target-nums[i]
            print("temp",i, nums[i], temp)
            if temp in nums and nums.index(temp)!=i:
                res.append(i)
                res.append(nums.index(temp))
                return res
    


       

        