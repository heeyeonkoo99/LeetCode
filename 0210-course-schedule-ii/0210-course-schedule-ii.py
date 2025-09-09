class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre=[[] for _ in range(numCourses)]
        nums=[0 for _ in range(numCourses)]
        ans=[]
        q=[]
        for i in prerequisites:
            pre[i[1]].append(i[0])
            nums[i[0]]+=1
        for i in range(len(nums)):
            if nums[i]==0:
                q.append(i)
        while q:
            value=q.pop()
            ans.append(value)
            for connect in pre[value]:
                nums[connect]-=1
                if nums[connect]==0:
                    q.append(connect)
        if len(ans)==numCourses:
            return ans
        return []



        