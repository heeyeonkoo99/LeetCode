class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        cnt=1
        points.sort(key=lambda x:x[1])

        temp=points[0][1]

        for p in range(1,len(points)):
            if temp<points[p][0]:
                cnt+=1
                temp=points[p][1]
            else:
            


        return cnt