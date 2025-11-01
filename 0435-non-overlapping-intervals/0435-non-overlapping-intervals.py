class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])

        cnt=0
        prev_end=float("-inf")

        for interval in intervals:
            start, end = interval

            if start>=prev_end:
                prev_end=end
            else:
                cnt+=1
        return cnt
        