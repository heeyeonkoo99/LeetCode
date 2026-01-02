class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res=[intervals[0]]
        intervals.sort(key=lambda x:x[0])
   
        for i in range(1,len(intervals)):
            if intervals[i][0]>res[-1][-1]:
                res.append(intervals[i])
            else:
                res[-1][1]=max(res[-1][1], intervals[i][1])
        return res
        