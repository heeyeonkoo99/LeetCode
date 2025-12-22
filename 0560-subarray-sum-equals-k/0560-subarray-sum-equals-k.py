class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result=0
        d={0:1}
        prefix_sum=0
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in d:
                result+=d[prefix_sum-k]
            d[prefix_sum]=d.get(prefix_sum,0)+1
        return result
