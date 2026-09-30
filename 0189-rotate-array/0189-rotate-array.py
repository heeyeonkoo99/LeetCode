class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=len(nums)%k
        a=nums[k:]+nums[:k]
        print(a)
        return a

        