class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        temp=set()

        for i in range(len(nums)):
            if nums[i] in temp:
                return True
            temp.add(nums[i])
            if len(temp)>k:
                temp.remove(nums[i-k])
        return False