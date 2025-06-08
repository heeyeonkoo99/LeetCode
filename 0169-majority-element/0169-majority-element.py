from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp=Counter(nums)
        print(temp)
        max=0
        answer=0
        for i in temp:
            if temp[i]>=max:
                max=temp[i]
                answer=i
        return answer
        