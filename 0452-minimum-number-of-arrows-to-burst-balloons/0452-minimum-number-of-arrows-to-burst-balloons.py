class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        cnt=1
        points.sort(key=lambda x:x[1])
        if not points:
            return 0
        i,n=0,len(points)
        temp=points[0][1]
        while i<n:
            if temp<=points[i][1]:
                continue
            else:
                temp=points[i][1]
                cnt+=1
        return cnt