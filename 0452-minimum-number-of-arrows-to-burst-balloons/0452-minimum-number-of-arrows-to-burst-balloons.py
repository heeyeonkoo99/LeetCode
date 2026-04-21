class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        cnt=1
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        temp=points[0][1]

        for i in range(1,len(points)):
            if temp<points[i][0]:
                cnt+=1
                temp=points[i][1]
                
            else:
                continue
        return cnt
        