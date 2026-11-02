class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        cnt=1
        points.sort(key=lambda x:x[1])
        end=points[0][1]
        for i in range(len(points)):
            if points[i][0]>end:
                cnt+=1
                end=points[i][1]
        return cnt
        