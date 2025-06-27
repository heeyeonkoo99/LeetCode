class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        - 처음생각: 먼저 twopointer로 모든 3자리 조합을 구해야하나..?? 근데 closet이니까 딱 정해진 target이 아니다..
          업데이트조건을 어떻게 정해야하지..?
        - 풀이: two pointer를 써서 abs로 가장 가까운값을 update해준다! 넘 어렵게 생각말기~~
        """
        best_s=1000000 # initialize with 3 sum number
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if s==target:
                    return s
                if abs(target-s)<abs(target-best_s):
                    best_s=s
                if s<=target:
                    left+=1
                    while left< right and nums[left]==nums[left-1]: # 이제 막 left+=1를 해주었으니까 left와 left-1의 값을 비교해준다.
                        left+=1
                else:
                    right-=1
        return best_s

        