
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=[]
        a=set(nums1)
        b=set(nums2)

        for i in a:
            if i in b:
                res.append(i)
        
        
        return res
        