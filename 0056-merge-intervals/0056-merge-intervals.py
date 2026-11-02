class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]

        for i in range(1,len(intervals)):
            if res[-1][1]<intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1]=max(res[-1][1],intervals[i][1])

        return res
        