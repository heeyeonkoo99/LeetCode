class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        i=1
        while i<len(intervals):
            
            if res[-1][1]>=intervals[i][0]:
                res[-1][1]=max(res[-1][1],intervals[i][1])
              
            else:
                res.append(intervals[i])
            i+=1

        return res
        