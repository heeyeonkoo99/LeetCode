class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        current_end=0
        farthest=0
        jumps=0

        for i in range(n-1):
            farthest=max(farthest,i+nums[i] )
            if i==current_end:
                jumps+=1
                current_end=farthest
        return jumps
        